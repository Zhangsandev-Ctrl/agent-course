### 今日目标

把账本的 JSON 读取逻辑升级为容错版：区分「单条脏记录」和「整个 JSON 文件损坏」两种情况。语法正常但字段非法的账目自动剔除；JSON 语法损坏时先备份坏文件，再以空账本启动，程序不崩溃、不丢原始坏文件。

### 核心知识点

1. **os 模块与 os.rename()**
   `os` 是 Python 自带的操作系统模块，负责文件、文件夹层面的操作。本项目用 `os.rename("account.json", "account_broken.json.bak")` 把损坏文件改名备份，保留原始坏文件便于事后找回，而不是直接删除。

2. **两层异常边界**

   - `FileNotFoundError`：账本文件压根不存在。处理：直接返回空列表 `[]`，程序正常新建空账本。
   - `json.JSONDecodeError`：文件存在，但里面的文本不符合 JSON 语法（缺逗号、引号、括号错乱）。处理：先 `os.rename` 备份成 `.bak`，再返回空列表，保护原始坏文件不被覆盖清空。

3. **单条脏数据逐条校验**
   JSON 语法能正常解析时，遍历 `raw_list` 逐条校验，只有三条规则全部通过才加入干净列表：

   - 这条必须是字典（`isinstance(item, dict)`）；
   - 必须包含 `r_type`、`money`、`remark` 三个必填 key；
   - `money` 必须是 `int / float` 数字（`bool` 要排除，不能当成金额）。

   不合规的条目 `dirty_count += 1` 跳过，其余合法记录照常保留。

4. **脏数据计数与自动清理**
   `load_records` 返回 `(干净列表, 脏数据条数)`。main 启动后如果 `dirty_count > 0`，调用 `save_records(干净列表)` 覆盖写回文件，脏数据就被永久清除；没有脏数据则不重复写文件。

5. **安全原则**
   语法合法的脏记录可以逐条剔除；整个文件语法损坏时程序一条都读不出来，无法判断哪条脏，所以不能擅自清空覆盖，必须先备份再重建空账本。

### 关键代码片段

```python
import json
import os

def load_records():
    try:
        with open("account.json", "r", encoding="utf-8") as f:
            raw_list = json.load(f)
    except FileNotFoundError:
        return [], 0
    except json.JSONDecodeError:
        backup_name = "account_broken.json.bak"
        os.rename("account.json", backup_name)
        print(f"⚠️ JSON文件损坏，已备份为 {backup_name}，将使用空账本启动")
        return [], 0

    record_list = []
    dirty_count = 0
    for item in raw_list:
        if not isinstance(item, dict):
            dirty_count += 1
            continue
        if "r_type" not in item or "money" not in item or "remark" not in item:
            dirty_count += 1
            continue
        if isinstance(item["money"], bool) or not isinstance(item["money"], (int, float)):
            dirty_count += 1
            continue
        record_list.append(item)
    return record_list, dirty_count
```

```python
def main():
    record_list, dirty_count = load_records()
    if dirty_count > 0:
        save_records(record_list)
        print(f"✅ 检测到 {dirty_count} 条脏账目，已经自动清理")
    # 下面进入 while 菜单循环
```

### 口述自测题与标准答案

**1. 问：JSONDecodeError 和 FileNotFoundError 分别是什么，处理策略有什么不同？**

答：
- `FileNotFoundError`：目标 JSON 文件不存在。处理：直接返回空列表，程序正常启动空账本。
- `JSONDecodeError`：文件存在，但内容不符合 JSON 语法、格式损坏。处理：先用 `os.rename` 把损坏文件改名备份成 `.bak`，再返回空列表，程序以空账本继续运行，保护原始坏文件不丢失。

**2. 问：为什么单条脏记录可以直接剔除，整个文件 JSON 损坏不能直接清空？**

答：JSON 语法正常时，程序能完整读取列表，循环逐条校验，单独把非法脏记录剔除，保留剩下的合法账目；整个文件语法损坏时，程序一条数据都读不出来，无法区分哪些是脏数据，所以不能直接清空，优先备份原文件，再启用空账本，避免原始数据直接丢失。

**3. 问：os.rename 在这个项目里起到什么作用？**

答：把损坏的 `account.json` 改名备份成 `.bak` 备份文件，留存原始损坏数据，防止数据直接丢失；备份完成后程序再使用空账本继续运行。

### 错题摘录（同步 error_book.md）

1. 报错：`TypeError: 'NoneType' object is not iterable`
   原因：JSON 损坏分支返回 `None`，main 判断后没有 `exit()` 阻断，代码继续进菜单，把 `None` 传给 `show_all` 做 for 遍历。
   解决：拿到 `None` 必须终止程序；D14 重构后损坏分支改为备份并返回空列表，不再返回 `None`。

2. 坑：清理脏数据时把全部数据清空
   原因：JSONDecodeError 分支直接返回空列表，随后触发自动 save 覆盖写入，把正常数据一起覆盖；或校验条件 key 名对不上，合法记录被误判为脏数据。
   解决：文件损坏时禁止直接覆盖写入；校验 key 名必须和 JSON 里的字段保持一致；清理前先遍历打印确认哪些记录被判脏。

3. 坑：多值解包报错 `not enough values to unpack`
   原因：`load_records` 各异常分支 return 的值个数不一致，有的只返回列表，有的返回两个值，解包时数量对不上。
   解决：所有出口统一返回 `(列表, 脏数据条数)` 成对值。
