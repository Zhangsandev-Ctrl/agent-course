# Python 基础 + 账本项目 · 面试复习手册

> 用途：把 D1–D16 全部 md 笔记去重合并成一份，供日常复习和面试口述使用。
> 覆盖：Python 基础语法、文件与 JSON、异常处理、模块拆分、Git、个人账本项目。
> 用法：先看「一、语法速查」建立框架，再看「四、面试问答」练口述，最后用「六、自测清单」验收。

---

## 一、语法速查

### 1. 变量与数据类型

| 类型 | 说明 | 示例 |
|---|---|---|
| `int` | 整数 | `90` |
| `float` | 小数 | `85.5` |
| `str` | 字符串，必须加引号 | `"优秀"` |
| `bool` | 布尔，只有 `True` / `False`，首字母大写 | `True` |

- `type(变量)`：查看变量类型。
- `=` 是赋值，`==` 是判断相等，两个不要混。
- 命名规则：字母、数字、下划线，不能数字开头，见名知义。
- 可变与不可变（面试常问）：`list` / `dict` 可变；`str` / `int` / `float` / `tuple` 不可变，字符串"修改"实际是生成新字符串。

### 2. 运算符

| 运算符 | 含义 | 示例 |
|---|---|---|
| `+ - * /` | 加减乘除，`/` 结果一定是小数 | `7 / 2 = 3.5` |
| `//` | 整除，只要商 | `7 // 2 = 3` |
| `%` | 取余 | `7 % 2 = 1` |
| `**` | 乘方 | `2 ** 3 = 8` |

- `+` 在字符串里是拼接，`*` 是重复：`"ab" * 3` → `"ababab"`。
- 字符串和数字不能直接相加，会报 `TypeError`。

### 3. 字符串

**取值**
- 索引 `s[0]`：从 0 开始，`s[-1]` 取最后一个。
- 切片 `s[1:3]`：左闭右开，取到下标 1、2，不含 3。
- `len(s)`：字符个数。
- `\n` 换行，`\t` 制表符。

**常用方法**

| 分类 | 方法 | 作用 |
|---|---|---|
| 空白 | `strip()` / `lstrip()` / `rstrip()` | 去两端 / 左侧 / 右侧空白 |
| 大小写 | `upper()` / `lower()` / `title()` | 全大写 / 全小写 / 首字母大写 |
| 判断 | `startswith()` / `endswith()` | 是否以某内容开头 / 结尾 |
| 判断 | `isalpha()` / `isdigit()` / `isalnum()` / `isspace()` | 纯字母 / 纯数字 / 字母数字 / 纯空白 |
| 切割 | `split(分隔符)` / `splitlines()` | 切成列表 / 按换行切 |
| 拼接 | `"连接符".join(列表)` | 列表拼成字符串，和 split 反向 |
| 替换 | `replace(old, new)` | 全部匹配项替换 |
| 查找 | `find()` / `index()` / `count()` | 找下标（找不到返回 -1）/ 找不到报错 / 统计次数 |

**`isdigit()` 的坑（金额校验高频）**：只认 0–9 组成的字符串，`"78.5"`、`"-100"` 一律返回 `False`，所以金额校验要用 `try + float()`，不能用 `isdigit()`。

**格式化**
- `f"总收入：{income:.2f}"`：`.2f` 固定保留两位小数。
- `input()` 返回值**永远是字符串**，参与计算前必须 `int()` 或 `float()`。

### 4. 条件判断

```python
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
else:
    print("继续努力")
```

- `if / elif / else` 行末尾必须写英文冒号，下一行必须缩进。
- 从上往下匹配，命中一个分支就跳出，不再判断后面的。
- 区间判断要用 `and`，不能写 `score >= 80 or score <= 89`（这个条件恒成立，逻辑废掉）。
- 三元表达式：`text = "是" if flag else "不是"`。
- `if is_student:` 等价于 `if is_student == True:`。

### 5. 循环

| 场景 | 用哪个 |
|---|---|
| 提前知道次数（遍历列表、`range`） | `for` |
| 不知道次数，只看条件是否成立 | `while` |

- `range(5)` → 0~4；`range(2, 6)` → 2~5；`range(1, 10, 2)` → 1,3,5,7,9。
- `range` 左闭右开，想包含 N 要写 `N + 1`；参数只能放数字，不能放列表。
- `break` 立刻跳出整个循环；`continue` 跳过本次、进入下一次。
- `while True` 常用来写菜单循环，靠 `break` 退出。

**两种经典编程思维（面试常考）**
1. **打擂台求最值**：先拿第一个元素当标杆，循环逐个比较，更大就替换。
```python
max_score = score_list[0]
for score in score_list:
    if score > max_score:
        max_score = score
```
2. **flag 标记查找**：可能存在多个结果时不能 `break`，用标记记录是否找到。
```python
has_find = False
for stu in stu_list:
    if stu["name"].startswith("张"):
        has_find = True
        print(stu)
if not has_find:
    print("没有找到")
```

### 6. 列表 list

```python
record_list = [
    {"r_type": "收入", "money": 100.0, "remark": "工资"},
    {"r_type": "支出", "money": 20.0, "remark": "奶茶"},
]
```

| 操作 | 写法 | 说明 |
|---|---|---|
| 追加 | `list.append(x)` | 末尾加一个元素，原地修改 |
| 插入 | `list.insert(idx, x)` | 指定位置插入 |
| 删除 | `del list[idx]` | 按下标删，**不返回**被删值 |
| 删除 | `list.pop(idx)` | 按下标删，**返回**被删值 |
| 删除 | `list.remove(值)` | 删第一个匹配值 |
| 排序 | `sort()` / `reverse()` | 原地排序 / 反转 |
| 统计 | `len()` / `count()` / `index()` | 长度 / 出现次数 / 找下标 |
| 遍历 | `enumerate(list)` | 同时拿到下标 `idx` 和元素 `item` |

- 下标从 0 开始，给用户看的序号要 `idx + 1`。
- 遍历时不要边遍历边删元素，容易漏项。
- 切片 `list[1:3]` 同样左闭右开。

### 7. 字典 dict

```python
item = {"r_type": "收入", "money": 100.0, "remark": "工资"}
item["money"]        # 取值，key 不存在会报 KeyError
item.get("note", "") # 安全取值，不存在返回默认值
```

- 新增/修改：`item["key"] = 值`；删除：`del item["key"]`。
- `keys()` / `values()` / `items()`：取键 / 取值 / 取键值对。
- 遍历：`for k, v in item.items():`。
- 字典适合"一条记录多个字段"，列表适合"多条同类记录"，账本 = 列表套字典。

### 8. 函数

```python
def add_record(record_list, r_type, money, remark):
    """新增一条账目记录。

    参数:
        record_list: list，账目列表
        r_type: str，"收入"或"支出"
        money: float，金额
        remark: str，备注
    返回:
        bool: True 表示添加成功
    """
    record_list.append({"r_type": r_type, "money": money, "remark": remark})
    return True
```

- `print` 只是打印给人看，`return` 才把值交回调用处；`return` 执行后函数立即结束。
- `return a, b, c` 返回的是**元组**；接收变量个数必须一致，否则报 `ValueError`（`too many / not enough values to unpack`）。
- 参数三类：位置参数（按顺序）、默认参数（有默认值，必须写在位置参数后）、关键字参数（`名=值`，顺序可换）。
- `*args` 收集位置参数成元组，`**kwargs` 收集关键字参数成字典（会读即可）。
- 作用域：局部变量只在函数内有效；全局变量函数内默认只读，要改必须 `global`。
- **优先用参数传递数据，不用全局变量**：作用域清晰、避免互相覆盖、函数可复用可测试。
- docstring 写在 `def` 下一行、三引号包裹，`help(函数名)` 能读出来；`#` 注释会被解释器忽略。

### 9. 异常处理

```python
try:
    age = int(input("年龄："))
except ValueError:
    print("年龄必须是数字")
else:
    print("录入成功")
finally:
    print("本次录入结束")
```

| 关键字 | 作用 |
|---|---|
| `try` | 放可能出错的代码 |
| `except` | 捕获指定异常，给友好提示 |
| `else` | 没有异常时才执行 |
| `finally` | 不管成功失败都执行，常用于释放资源 |

- 常见异常：`ValueError`（转换失败）、`KeyError`（字典没这个键）、`IndexError`（下标越界）、`TypeError`（类型不匹配）、`FileNotFoundError`（文件不存在）、`json.JSONDecodeError`（JSON 格式坏了）。
- 多分支顺序：**具体异常在前，宽泛的 `Exception` 放最后**，否则后面永远捕获不到。
- `raise ValueError("金额必须大于0")`：业务规则不满足时主动抛出。
- `if` 与 `try` 的选择：可预见的业务规则用 `if` 提前拦截；类型转换、文件读取这类不可控操作用 `try/except` 兜底。

### 10. 文件与 JSON

```python
with open("account.json", "r", encoding="utf-8") as f:
    data = json.load(f)
```

- `with` 上下文管理器：执行完或中途报错都会**自动关闭文件**，不用手写 `close()`。
- 打开模式：`r` 只读、`w` 覆盖写、`a` 追加写；账本必须用 `w` 全量覆盖，用 `a` 会数据重复叠加。
- `encoding="utf-8"` 避免中文乱码。

**四个方法必须分清（高频考点）**

| 方法 | 方向 |
|---|---|
| `json.dump(obj, f)` | Python 对象 → 写入文件 |
| `json.dumps(obj)` | Python 对象 → 转成 JSON 字符串（调试打印用） |
| `json.load(f)` | 文件里的 JSON → Python 对象 |
| `json.loads(s)` | JSON 字符串 → Python 对象 |

- `ensure_ascii=False`：中文正常显示，不转成 `\uXXXX`。
- `indent=2`：格式化缩进，文件可读。
- JSON 只支持字符串、数字、列表、字典、bool、null，不能直接存自定义对象。

**两层容错（账本核心设计）**

```python
try:
    with open(ACCOUNT_FILE, "r", encoding="utf-8") as f:
        raw_list = json.load(f)
except FileNotFoundError:
    return [], 0                      # 文件不存在：空账本
except json.JSONDecodeError:
    os.rename(ACCOUNT_FILE, backup)   # 文件语法坏了：先备份再空账本
    return [], 0
```

- 语法合法、只是单条字段非法 → 逐条校验剔除，脏数据计数，干净列表覆盖写回，脏数据被永久清掉。
- 整个文件语法损坏 → 读不出任何一条，**不能擅自清空覆盖**，先 `.bak` 备份再重建空账本。

### 11. 模块与依赖

```python
import json                          # 整个模块，调用要带前缀 json.load()
from storage import load_records     # 只导入函数，直接调用 load_records()
```

- 一个 `.py` 文件就是一个模块，模块名 = 文件名去掉 `.py`，必须逐字母一致（`load_record` 和 `load_records` 是两个名字）。
- 循环导入：两个模块互相 import，形成闭环，加载时一方还没加载完就报 `ImportError`。
- 依赖保持单向：`main` → `storage / ledger / utils`，底层模块不反向依赖上层。
- `requirements.txt`：记录第三方库及版本，别人 `pip install -r requirements.txt` 一键装环境；标准库 `json` / `os` 不用写。
- `.gitignore`：不提交缓存（`__pycache__/`、`*.pyc`）、虚拟环境（`.venv/`）、密钥（`.env`）、编辑器配置（`.idea/`）、系统文件（`.DS_Store`）。

---

## 二、个人账本项目（第一个可讲的项目）

### 1. 功能清单

- 新增收支：收支类型、金额、备注三重校验
- 查看全部账目（序号从 1 开始）
- 计算总收入、总支出、余额（保留两位小数）
- 删除账目（序号校验 + y/n 二次确认）
- 修改账目（展示旧数据 + 重新录入 + 确认）
- JSON 持久化，重启数据不丢
- 容错：文件缺失、文件损坏、单条脏数据都能兜住

### 2. 三层架构（面试重点）

| 文件 | 职责 | 边界 |
|---|---|---|
| `main.py` | 菜单交互、输入校验、决定是否保存 | 不写业务计算、不直接读写文件 |
| `ledger.py` | 增删改查、余额计算 | 只操作传入的列表，**不碰文件** |
| `storage.py` | JSON 读写、脏数据校验、损坏备份 | 不关心业务规则 |
| `utils.py` | 通用小工具（如 `is_valid_money`） | 不依赖任何业务模块 |

依赖方向单向：`main` → `ledger` / `storage` / `utils`，无循环导入。

### 3. 三个关键设计（能讲清就加分）

**① `changed` 布尔标记**
业务函数改完列表返回 `True`，取消或失败返回 `False`；`main` 只在 `True` 时调用 `save_records`，避免无效 IO 和"没改也写文件"。

**② 脏数据逐条过滤**
`json.load` 只保证语法合法，不保证字段合法。加载后逐条校验：必须是字典、三个 key 齐全、`money` 是数字（排除 `bool`）。合法进列表，非法 `dirty_count += 1`，清理后覆盖写回。

**③ 数据文件路径不依赖启动目录**
```python
def _find_account_file():
    cur = os.path.dirname(os.path.abspath(__file__))
    while True:
        candidate = os.path.join(cur, "account.json")
        if os.path.exists(candidate):
            return candidate
        parent = os.path.dirname(cur)
        if parent == cur:
            return os.path.join(cur, "account.json")
        cur = parent
```
`__file__` 是当前脚本自身路径（前后各两个下划线，Python 内置特殊变量）；基于它向上找文件，从任何目录启动都不会找不到。

### 4. 项目怎么讲（30 秒口述模板）

> 这是我用纯 Python 写的命令行个人账本，支持收支新增、查看、余额统计、删除和修改，数据用 JSON 持久化。
> 代码按职责拆成四个文件：main 负责菜单交互，ledger 只做业务计算，storage 只管文件读写，utils 放通用工具，依赖是单向的，没有循环导入。
> 有两个设计点我印象比较深：一是业务函数用布尔返回值告诉主程序"数据有没有变"，只有变了才写文件；二是读取时做了两层容错——单条字段非法就逐条剔除并覆盖写回，整个 JSON 语法损坏就先备份成 .bak 再启空账本，不会把原始数据冲掉。
> 过程中踩过的坑主要是不分层（业务函数里直接写文件）、多返回值解包数量不一致、变量名拼写错误导致 NameError，这些我都记在错题本里复现过。

---

## 三、Git 与工程习惯

| 命令 | 作用 |
|---|---|
| `git init` | 初始化仓库 |
| `git status` | 看当前改动状态 |
| `git add .` | 全部改动加入暂存区 |
| `git commit -m "说明"` | 生成一次本地提交 |
| `git push` | 推送到远程仓库 |
| `git log --oneline` | 查看提交历史 |

- commit message 要写清"改了什么"，不写无意义的 `update`，例如 `D16 模块拆分与依赖管理，抽取utils工具模块`。
- `nothing to commit, working tree clean`：没有新改动，不是报错。
- `Everything up-to-date`：本地没有新 commit，没内容可推。
- `Recv failure: Connection was reset`：网络问题，commit 已保存在本地，重试 push 或换网络。
- 不提交 `__pycache__/`、`*.pyc`、`.venv/`、`.env`、模型文件、本地数据文件。

---

## 四、高频面试问答（25 题）

### A. 基础语法

**1. `=` 和 `==` 的区别？**
`=` 是赋值，把右边的值装进左边变量；`==` 是判断两边是否相等，结果是 `True` / `False`。

**2. `input()` 返回什么类型？做计算要注意什么？**
永远返回字符串 `str`；参与数学运算前必须 `int()` 或 `float()` 转换，否则报 `TypeError`。

**3. `/`、`//`、`%`、`**` 分别是什么？**
`/` 除法（结果带小数）、`//` 整除只留商、`%` 取余数、`**` 乘方。

**4. `if` 的区间判断为什么不能用 `or`？**
`score >= 80 or score <= 89` 对任何数字都成立，条件恒真。区间要用 `and` 同时满足上下界。

**5. `for` 和 `while` 怎么选？**
次数已知、遍历序列用 `for`；次数未知、只看条件成立与否用 `while`。

**6. `break` 和 `continue` 的区别？**
`break` 直接跳出整个循环；`continue` 只结束本次，进入下一次循环。

**7. `range` 的几个坑？**
左闭右开，要包含 N 得写 `N+1`；参数只能是整数，不能放列表。

### B. 数据结构

**8. 列表和字典分别适合什么场景？**
列表适合存多条同类数据、需要顺序和增删；字典适合存一条数据的多个字段，靠 key 快速取值。账本就是"列表套字典"。

**9. `del` 和 `pop()` 的区别？**
都按下标删；`del` 不返回值，`pop()` 会把删掉的值返回。

**10. `append()` 和 `insert()` 的区别？**
`append()` 追加到末尾；`insert(idx, x)` 插到指定位置。都是原地修改原列表。

**11. `enumerate()` 有什么用？**
遍历时同时拿到下标和元素：`for idx, item in enumerate(record_list):`，账本展示序号用 `idx + 1`。

**12. 怎么不用 `max()` 求列表最大值？**
打擂台：先拿第一个元素当标杆，循环逐个比较，更大就替换。

**13. 遍历查找多个结果时为什么不能用 `break`？**
`break` 找到第一个就跳出，会漏掉后面的匹配项；多结果场景要用 `flag` 标记是否找到，遍历完整。

**14. 字符串、列表、元组哪些可变？**
字符串、元组不可变，列表、字典可变。字符串"修改"实际是生成新字符串。

### C. 函数

**15. `print` 和 `return` 的区别？**
`print` 只把内容打印到终端，函数外拿不到；`return` 把值交回调用处，可以赋值给变量，执行后函数立即结束。

**16. `return a, b` 返回的是什么？**
返回一个元组；接收时变量个数必须和返回值个数一致，否则 `ValueError`。

**17. 位置参数、默认参数、关键字参数的区别？**
位置参数按顺序传、必填在前；默认参数有默认值、可省略，且必须写在位置参数后面；关键字参数调用时写 `名=值`，顺序可调换。

**18. 局部变量和全局变量的区别？**
局部变量只在函数内有效；全局变量定义在函数外，函数内默认只读，修改要 `global` 声明。

**19. 为什么不建议用全局变量传数据？**
作用域不清、多个函数容易互相覆盖、函数脱离全局数据就无法复用和测试。数据走参数进出更清晰。

**20. docstring 和 `#` 注释的区别？**
docstring 写在 `def` 下一行、三引号包裹，属于函数对象的一部分，`help()` 能读取；`#` 注释是给人看的，解释器直接忽略。

### D. 异常与文件

**21. `try / except / else / finally` 各自作用？**
`try` 放可能出错的代码；`except` 捕获异常给提示；`else` 没异常时执行；`finally` 无论如何都执行，常用来释放资源。

**22. 多个 `except` 的书写顺序要注意什么？**
具体异常写前面，宽泛的 `Exception` 放最后，否则后面的分支永远匹配不到。

**23. `ValueError`、`KeyError`、`IndexError`、`FileNotFoundError` 什么时候出现？**
转换失败（`int("abc")`）、字典取不存在的 key、列表下标越界、打开的文件不存在。

**24. `with open()` 的好处？**
执行完或中途报错都会自动 `close()`，不用手写，避免文件句柄泄露和文件被占用。

**25. `json.dump` 和 `json.dumps`、`json.load` 和 `json.loads` 的区别？**
带 `s` 的操作字符串：`dumps` 对象转 JSON 字符串、`loads` JSON 字符串转对象；不带 `s` 的操作文件：`dump` 写入文件、`load` 从文件读。

### E. 工程与项目

**26. 为什么要把代码拆成多个文件？**
职责单一、便于维护和复用。`main` 管交互、`ledger` 管业务、`storage` 管文件、`utils` 放工具，依赖单向，避免循环导入。

**27. 业务层为什么不直接读写文件？**
分层要求：业务层只操作传入的列表，返回布尔结果；是否落盘由入口层决定。否则会出现一次修改写多次文件、逻辑和 IO 耦合。

**28. `FileNotFoundError` 和 `JSONDecodeError` 的处理为什么不同？**
文件不存在是"没有数据"，直接空账本即可；文件存在但语法坏了说明"有数据但读不出来"，必须先备份原文件再重建，避免把还能恢复的数据冲掉。

**29. 什么叫脏数据？怎么处理？**
JSON 语法合法但记录字段非法（缺 key、类型不对、金额不是数字）。加载后逐条校验，非法的剔除并计数，干净列表覆盖写回文件。

**30. `__file__` 是什么？为什么用它定位文件？**
`__file__` 是当前脚本自身的路径（Python 内置特殊变量，前后各两个下划线）。相对路径依赖启动目录，换目录就找不到文件；基于 `__file__` 定位不受启动位置影响。

---

## 五、易错点清单（错题本精华）

| 报错 / 现象 | 根因 | 正确做法 |
|---|---|---|
| `ImportError: cannot import name` | 导入名和 `def` 定义名不一致（单复数、拼写） | 两边逐字母统一 |
| `NameError: name 'xxx' is not defined` | 调用在定义之前；漏传形参；变量名拼错 | 先定义后调用；`show_all(record_list)` 传参；统一命名 |
| `UnboundLocalError` | 分支路径变量未赋值 | 所有分支给初始值 |
| `TypeError: 'NoneType' object is not iterable` | 返回 `None` 后没终止，继续 for 遍历 | 检测到 `None` 立即 `exit()` |
| `TypeError: 'tuple' object has no attribute 'append'` | 多返回值未解包，元组当列表用 | `a, b = func()` 正确解包 |
| `ValueError: not enough values to unpack` | 各 return 出口返回值个数不一致 | 所有出口成对返回 |
| `IndentationError` | 函数体没缩进 / 缩进不一致 | `def` 下统一缩进 4 空格 |
| `dict` 取不存在的 key 报 `KeyError` | 直接 `[]` 取值 | 用 `.get(key, 默认值)` |
| 改了代码运行没变化 | 文件未保存，跑的是硬盘旧文件 | 改完 `Ctrl+S`，白点消失再跑 |
| 新建模块 0 字节 | 代码只在编辑器缓冲区 | 保存后再 import 测试 |
| 删除/修改后数据复原 | 只改内存没调 `save_records` | `changed` 为 `True` 时保存 |
| 清理脏数据把全部数据清空 | 损坏分支直接覆盖写入；校验 key 名不匹配 | 损坏先备份；key 名与 JSON 一致 |
| 找不到 `account.json` | 相对路径依赖启动目录 | 用 `__file__` 逐级向上定位 |
| `git push` 连接重置 | 网络波动 | commit 已存本地，重试 push |

---

## 六、复习自测清单

### 第一轮：语法（能默写代码）
- [ ] 手写 `if / elif / else` 三段式，缩进和冒号正确
- [ ] 手写 `for + range` 求 1~100 偶数和
- [ ] 手写打擂台求最大值、flag 标记查找
- [ ] 说出列表 5 个常用方法及其返回值
- [ ] 说出字典 4 个常用方法，`get()` 的作用
- [ ] 写一个带 docstring、默认参数、返回多值的函数
- [ ] 写 `try / except / else / finally` 完整结构
- [ ] 写 `with open` 读 JSON 并捕获两类异常

### 第二轮：口述（不看笔记）
- [ ] 用 1~2 句话回答「四、面试问答」全部 30 题
- [ ] 讲清账本三层架构和三个关键设计
- [ ] 讲清 `dump / dumps / load / loads` 区别
- [ ] 讲清为什么要分层、业务层为什么不碰文件

### 第三轮：项目复现
- [ ] 不看原代码，从零重写 main / ledger / storage / utils
- [ ] 故意造一条脏数据，验证过滤逻辑
- [ ] 故意把 JSON 改坏，验证备份逻辑
- [ ] 用 Git 完整提交一次，commit message 规范

---

## 附：冗余处理说明

原笔记存在的问题（本次已在合并版中去重，未改动原文件）：

1. `day2.md` 内部重复：前半是「Day2 笔记」，后半又贴了一份「Day1 + Day2 合并笔记」，知识点重叠近 80%。
2. `day12.md` 混入 D13 内容：末尾贴了 JSON 进阶和 `dump/dumps` 两条，和 D12 主题混在一起；「知识点复盘」段落出现两次。
3. `day9.md` 的「错题摘录」和 `error_book.md` 内容重复。
4. `error_book.md` 中「D9 + D10 知识点&错题笔记」主体是知识点不是错题；「D12 今日报错总结」与「error_book.md 新增条目（D12）」两段重叠。
5. `day5.md`、`day8.md` 是代码片段碎片，缺上下文说明，已按知识点归并到本手册。
