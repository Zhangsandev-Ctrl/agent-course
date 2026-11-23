# Python 错题本

> 格式：日期 | 报错原文 | 原因分析 | 正确写法 | 关联知识点
> 规则：每个报错先记这里，再动手改；周末统一重做验证。
> 说明：本文件只放**报错和踩坑**，知识点正文已统一合并到《Python基础_面试复习手册.md》。

## 速查索引

| 报错 / 现象 | 一句话根因 | 条目位置 |
|---|---|---|
| `NameError` | 名字未定义：用在定义前、漏传参、变量名拼错 | D1、D12、D15、D16 |
| `UnboundLocalError` | 分支路径变量没赋值就使用 | D12 |
| `ImportError` | 导入名和定义名不一致 | D12 |
| `TypeError: 'NoneType' object is not iterable` | 返回 None 后没终止，继续遍历 | D14 |
| `TypeError: 'tuple' object has no attribute 'append'` | 多返回值没解包，元组当列表用 | D15 |
| `TypeError: unsupported operand` | 字符串和数字直接运算 | D2、D9 |
| `ValueError: not enough values to unpack` | 各 return 出口返回值个数不一致 | D14 |
| `IndentationError` | 函数体/分支体没缩进 | D16 |
| `KeyError` | 字典直接取不存在的 key | D9 |
| 数据不持久化 | 改完内存没调 `save_records` | D9、D12 |
| 清理脏数据全被清空 | 损坏分支直接覆盖写 | D14 |
| 读不到账本文件 | 相对路径依赖启动目录 | D15 |

---

## D1 · 2026-11-06 起步错题

### 1. 字符串没加英文双引号
- 报错原文：`NameError: name '岁' is not defined`
- 原因分析：`岁` 不加引号，Python 当成变量名去找，找不到就报错
- 正确写法：`print("明年我", next_year_age, "岁")`，文字必须包英文双引号
- 关联知识点：字符串 str / 变量

### 2. def 定义函数末尾漏冒号
- 报错原文：`SyntaxError: expected ':'`
- 原因分析：`def 函数名(...)` 这一行结尾必须有英文冒号
- 正确写法：`def add(a, b):`
- 关联知识点：函数定义 / 语法

### 3. 调用函数被缩进到函数内部
- 报错原文：无报错但函数内容不打印
- 原因分析：`introduce()` 前面有缩进，被当成函数体里的代码，不会自动执行
- 正确写法：`introduce()` 顶格写，和 `def` 对齐
- 关联知识点：缩进 indentation

### 4. 改完代码没保存就运行
- 报错原文：结果还是旧的，看不到修改效果
- 原因分析：VSCode 标签页出现白点 `U` 表示未保存，Python 运行的是硬盘上的旧文件
- 正确写法：每次改完按 `Ctrl+S`，白点消失再运行
- 关联知识点：文件保存

---

## D2 · 语法与逻辑坑

### 5. f-string 漏写 f
- 报错原文：`print("你好，我叫{name}，今年{age}岁")` 输出原样花括号
- 原因分析：字符串前少写 `f`，变量不会被替换
- 正确写法：`f"你好，我叫{name}，今年{age}岁"`
- 关联知识点：f-string 格式化

### 6. 区间判断误用 or（逻辑错误）
- 报错原文：无报错，但 80~89 的分段永远跑不到
- 原因分析：`score >= 80 or score <= 89` 对任何数字都成立，条件恒真
- 正确写法：`score >= 80 and score <= 89`
- 关联知识点：and / or 区别；同时满足用 `and`，满足任意一个用 `or`

### 7. 中文字符当代码符号
- 报错原文：`SyntaxError: invalid character`
- 原因分析：用了中文冒号 `：`、中文引号 `“”`
- 正确写法：代码内一律英文冒号 `:`、英文引号 `""`
- 关联知识点：语法符号

### 8. `TypeError: unsupported operand type(s) for /: 'str' and 'str'`
- 原因分析：`input()` 返回字符串，两个字符串不能做除法
- 正确写法：`float(input("身高："))` 先转数字
- 关联知识点：input 返回值类型、类型转换

### 9. `NameError: name 'BMI' is not defined`（变量写在分支内）
- 原因分析：`BMI` 定义在 `else` 里，走 `if` 分支时这个变量根本不存在
- 正确写法：后面要用的变量提到分支外层，先赋初值
- 关联知识点：变量作用域

### 10. `msg.strip.upper()` 报错
- 原因分析：方法没带括号，拿到的是方法对象不是结果
- 正确写法：`msg.strip().upper()`
- 关联知识点：方法调用必须带 `()`

---

## D9–D10 · 账本雏形（列表 + 字典 + 文件）

### 11. `TypeError: unsupported operand type(s) for +: 'int' and 'str'`
- 原因分析：`input()` 拿到字符串，没转数字就参与累加
- 正确写法：`int()` / `float()` 转换后再计算
- 关联知识点：类型转换

### 12. 下标偏移（用户序号 vs 列表下标）
- 现象：输入序号 1 删掉了第 2 条
- 原因分析：用户从 1 数，列表从 0 开始
- 正确写法：`idx = num - 1`
- 关联知识点：索引、越界保护

### 13. 删除 / 修改后忘记保存
- 现象：内存里删了，重启程序账目又回来
- 原因分析：只改了内存列表，没调用 `save_records()`
- 正确写法：改动成功后调用保存，用 `changed` 标记控制
- 关联知识点：持久化、内存 vs 文件

### 14. `KeyError`（字典取不存在的键）
- 原因分析：直接用 `item["note"]` 取没写过的 key
- 正确写法：`item.get("note", "")` 安全取值
- 关联知识点：dict.get()

### 15. 把 print 当 return 用
- 现象：函数外面拿不到计算结果
- 原因分析：函数里只 `print`，没有 `return`
- 正确写法：`return total, avg`，外部解包接收
- 关联知识点：print 是展示，return 是传回数据

### 16. try-except 范围过大
- 原因分析：把整个业务逻辑都包进 try，出错时分不清是哪一步
- 正确写法：只包可能出错的那一两行（如 `int(input())`）
- 关联知识点：异常捕获粒度

### 17. Git 报 `pathspec ... did not match any files`
- 原因分析：`git add` 路径写错或文件不存在
- 正确写法：写完整相对路径，先 `git status` 确认
- 关联知识点：Git 暂存区

### 18. `isdigit()` 判小数失败
- 现象：输入 `10000.34` 被判非法
- 原因分析：`isdigit()` 只认纯数字字符串，小数点、负号一律 False
- 正确写法：`try: float(input())` 捕获 `ValueError`，兼容整数和小数
- 关联知识点：字符串判断方法局限

---

## D12 · JSON 化与分层

### 19. `ImportError: cannot import name 'load_records' from 'storage'`
- 原因分析：模块里定义的是 `load_record`（少 s），main 导入写的是 `load_records`
- 正确写法：两边命名统一，推荐都用复数 `records`
- 关联知识点：模块导入、命名一致性

### 20. `NameError: name 'record_list' is not defined`（漏传参）
- 原因分析：`delete_record` 里调用 `show_all()` 没传列表，函数内拿不到
- 正确写法：`show_all(record_list)`
- 关联知识点：函数形参、局部作用域

### 21. `UnboundLocalError: cannot access local variable 'r_type'`
- 原因分析：三段 while 输入校验缩进错乱，`r_type` 未赋值就传给 `add_record`
- 正确写法：三段校验全部写在 `if choice == "1":` 内部，全部通过后再调用新增
- 关联知识点：缩进、变量赋值路径

### 22. `UnboundLocalError`（异常分支变量名不一致）
- 报错原文：`cannot access local variable 'date' where it is not associated with a value`
- 原因分析：try 里写 `date`，except 分支赋值 `data`，return 写 `date`
- 正确写法：所有分支路径变量都有初始值，变量名全程统一
- 关联知识点：异常分支、变量作用域

### 23. 变量拼写错误 `recordf_list`
- 现象：形参多打一个字母 f，函数内部自洽所以不报错，但可读性差、易引发后续 `NameError`
- 正确写法：统一改回 `record_list`
- 关联知识点：命名规范

### 24. 分层错误：业务层直接写文件
- 现象：一次修改写了两次文件；保存逻辑散落各处
- 原因分析：`ledger` 里直接调用 `save_records`，业务层越界做 IO
- 正确写法：ledger 只改列表、返回 `True/False`；main 拿到 `changed` 为 True 才保存
- 关联知识点：分层设计、职责单一

### 25. 拿到 `changed` 却没判断
- 现象：删除/修改成功但数据没落盘
- 原因分析：main 只写了 `changed = delete_record(...)`，缺 `if changed:` 和 `save_records`
- 正确写法：所有写操作统一 `if changed: save_records(record_list)`
- 关联知识点：布尔返回值、持久化

### 26. `git push` 报 `Recv failure: Connection was reset`
- 原因分析：本地到 GitHub 网络波动
- 正确写法：commit 已存本地，重试 push 或换网络
- 关联知识点：Git 本地与远程

---

## D14 · JSON 容错重构

### 27. `TypeError: 'NoneType' object is not iterable`
- 原因分析：JSON 损坏分支返回 `None`，main 判断后没 `exit()`，继续把 `None` 传给 `show_all` 遍历
- 正确写法：检测到 `None` 立即 `exit()` 阻断；重构后损坏分支改为备份并返回空列表
- 关联知识点：异常分支返回值、可迭代对象

### 28. 清理脏数据把全部数据清空
- 现象：一执行清理，正常账目全部消失
- 原因分析：`JSONDecodeError` 分支直接返回空列表，随后触发自动 `save_records` 覆盖；或校验 key 名不匹配（`type` vs `r_type`），合法记录全被误判
- 正确写法：文件损坏时禁止直接覆盖写；校验 key 名与 JSON 字段完全一致；清理前逐条打印确认
- 关联知识点：脏数据过滤、数据安全兜底

### 29. `ValueError: not enough values to unpack (expected 2, got 1)`
- 原因分析：`load_records` 有的分支 `return []`，有的 `return [], 0`，解包数量对不上
- 正确写法：所有出口统一返回 `(record_list, dirty_count)`
- 关联知识点：多返回值、元组解包

### 30. `NameError: name 'os' is not defined`
- 原因分析：用了 `os.rename` 但没 `import os`
- 正确写法：文件顶部 `import os`
- 关联知识点：模块导入

### 31. 损坏文件处理原则
- 现象：删掉 `account.json` 能正常启动，文件存在但语法坏了却直接退出，误以为逻辑有问题
- 原因分析：两条分支语义不同——`FileNotFoundError` 是"没有数据"，`JSONDecodeError` 是"有数据但读不出来"
- 正确写法：不存在 → 空账本；语法损坏 → 先 `.bak` 备份再空账本，不能直接删
- 关联知识点：异常语义区分

---

## D15 · 启动读不到账单（专项排错）

### 32. `NameError: name 'data' is not defined`（模块顶层残留调试代码）
- 原因分析：调试用的 `print(data)`、`print(valid_list)` 写在函数外的模块顶层，`import storage` 时立即执行，变量从未定义
- 正确写法：临时调试打印放函数内部，调试完删除
- 关联知识点：模块导入即执行顶层代码

### 33. 校验循环漏 `append`，且 `return` 写在 for 内部
- 现象：JSON 合法、记录正常，加载出来永远是空列表
- 原因分析：合法记录没有 `record_list.append(item)`；`return` 写在循环体内，第一条处理完就提前返回
- 正确写法：`continue` 跳过脏数据，合法记录 append；`return` 放在循环外
- 关联知识点：循环结构、函数返回时机

### 34. 相对路径与运行目录不一致，找不到 `account.json`
- 现象：代码在 `day01\week1\`，数据文件在项目根目录；从 week1 启动就找不到文件，走 `FileNotFoundError` 返回空账本
- 原因分析：相对路径依赖当前工作目录 cwd
- 正确写法：用 `os.path.abspath(__file__)` 基于脚本自身位置逐级向上查找，不依赖 cwd
- 关联知识点：绝对/相对路径、`__file__`、os.path

---

## D16 · 模块拆分与缩进

### 35. `IndentationError: expected an indented block after function definition`
- 原因分析：`def is_valid_money(value):` 后面 docstring 和 `return` 顶格写，函数体没缩进
- 正确写法：函数体统一缩进 4 空格
- 关联知识点：缩进规则

### 36. 新建模块 0 字节，导入找不到函数
- 现象：编辑器里写好了函数，磁盘上 `utils.py` 大小为 0
- 原因分析：代码只在 VSCode 缓冲区，没按 `Ctrl+S`
- 正确写法：保存后再 import 测试
- 关联知识点：文件保存、模块导入前置条件

### 37. `NameError: name 'money' is not defined`（局部变量名写错）
- 原因分析：修改函数里变量叫 `new_money`，调用工具函数时误写成 `money`
- 正确写法：`if not is_valid_money(new_money):`
- 关联知识点：局部变量作用域、命名一致

### 38. 校验分支写反，try 里混入判断
- 现象：金额非法时反而 `break` 放行
- 原因分析：`if not is_valid_money(...)` 为 True 表示非法，应 `print + continue`；且 `float()` 转换与合法性判断挤在同一个 try 里
- 正确写法：try 只做 `float()`；`except ValueError` 里 `continue`；转换成功后 `if not 合法: print + continue`，最后 `break`
- 关联知识点：while 输入校验、try 边界、工具函数复用

---

## 跨项目通用坑点（不报错但必须记住）

1. **多处 `load_records()`** 会重复读文件、重复打印提示；启动只加载一次。
2. **文件写入模式**：账本必须 `w` 覆盖，用 `a` 会数据重复叠加。
3. **`isdigit()` 只能校验正整数**，金额一律用 `try + float()`。
4. **`strip()` 只去两端空白**，中间空格不受影响。
5. **`del` 不返回被删值**，需要返回值用 `pop()`。
6. **`enumerate` 的 idx 从 0 开始**，展示序号要 `idx + 1`。
7. **`return` 写在循环里会提前结束函数**，想汇总全部数据必须放循环外。
8. **模块顶层不要留调试 print**，`import` 时立刻执行。
