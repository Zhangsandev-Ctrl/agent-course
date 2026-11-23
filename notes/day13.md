### 今日目标

承接 D12 的 JSON 读写，搞清楚 `dump / dumps / load / loads` 的区别，理解 JSON 嵌套结构，并在读取阶段加入数据合法性校验，防止外部文件被改坏后程序崩溃。

### 核心知识点

1. **`dump / dumps`、`load / loads` 的区别（高频口述考点）**

| 方法 | 方向 | 使用场景 |
|---|---|---|
| `json.dump(obj, f)` | Python 对象 → 写入文件 | 保存账本 |
| `json.dumps(obj)` | Python 对象 → JSON 字符串 | 打印调试、网络传输 |
| `json.load(f)` | 文件里的 JSON → Python 对象 | 程序启动加载账本 |
| `json.loads(s)` | JSON 字符串 → Python 对象 | 接口返回值解析 |

> 带 `s` 的操作 **string（字符串）**；不带 `s` 的操作 **file（文件）**。

2. **格式化参数**
- `ensure_ascii=False`：中文正常显示，不转成 `\uXXXX`，账本必配。
- `indent=2`：缩进美化，保存出来的 JSON 一行一条、可读性好。

```python
json.dump(record_list, f, ensure_ascii=False, indent=2)
```

3. **JSON 嵌套结构**
JSON 支持字典套字典、列表套字典：
```python
{
  "name": "张三",
  "info": {"age": 20, "hobby": ["看书", "跑步"]}
}
```
账本正是"列表套字典"：外层列表存多条账目，每条账目是字典。

4. **JSON 的类型限制**
只支持字符串、数字、列表、字典、bool、null；**不能直接存自定义对象**，需要先转成字典。

5. **读取后的数据校验（脏数据过滤）**
`json.load` 只能保证语法合法，不能保证每条记录字段合法。加载后逐条校验：

- 必须是字典；
- 必须包含 `r_type`、`money`、`remark` 三个 key；
- `money` 必须是 `int / float`（`bool` 要排除）。

不合法就丢弃并计数 `dirty_count`，合法的进干净列表；有脏数据时用干净列表覆盖写回文件，脏数据被永久清除。

```python
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
```

6. **输入校验 vs 文件校验的分工**
- 用户输入时用 `if` / `while` 拦截：拦的是"人输错"。
- 文件读取后用校验函数兜底：拦的是"文件被改坏"。
两层都要有，缺一层就会出问题。

### 口述自测

1. `dump` 和 `dumps` 有什么区别？`load` 和 `loads` 呢？
2. `ensure_ascii=False` 和 `indent` 分别起什么作用？
3. 为什么 `json.load` 成功读取了文件，还要做字段校验？
4. 脏数据是怎么被永久清除的？
5. 输入校验和文件校验分别拦的是什么问题？
