# Python 错题本

> 格式：日期 | 报错原文 | 原因分析 | 正确写法 | 关联知识点
> 规则：每个报错先记这里，再动手改；周末周日统一重做验证。

## 2026-11-06

### 1. 字符串没加英文双引号
- 报错原文：`NameError: name '岁' is not defined`
- 原因分析：`岁` 不带引号，Python 把它当成变量名去找，找不到就报错
- 正确写法：`print("明年我", next_year_age, "岁")`，文字必须包英文双引号
- 关联知识点：字符串 str / 变量

### 2. def 定义函数末尾漏冒号
- 报错原文：`SyntaxError: expected ':'`
- 原因分析：`def 函数名(...)` 这一行结尾必须有英文冒号 `:`
- 正确写法：`def add(a, b):`
- 关联知识点：函数 function / 语法

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
# Day01 错题&知识点记录
1. def 函数：def 后面写函数名，末尾必须英文冒号，内部代码缩进，写完要调用才会执行
2. 变量：名字自己定义，等号=是赋值，不是数学等于
3. 4种基础类型：str字符串、int整数、float小数、bool布尔（True/False）
4. f-string格式化：f"内容{变量}"，可以把变量放进字符串里面
5. if 判断：if 条件:  冒号不能丢，内部代码必须缩进
   - if 布尔变量：`if is_student:` 等价 `if is_student == True:`
6. 三元表达式：`text = "是" if is_student else "不是"`
7. 踩过的坑：
   - 中文冒号、中文引号，直接报语法错误
   - 缩进不对，代码归属混乱
   - 定义函数之后忘记调用，代码不运行

day2 错题本
报错原文：print("你好，我叫{name},今年{age}岁，身高{height}米，我是{is_student}学生")
原因分析：缺少了f！（变量名）必须加f，叫f-string，不然会报错
if和else行末尾写：号
print前面要teb缩进
`=` 是赋值（给变量装东西）
`==` 是判断相等
`!=` 是判断不相等
致命错误：`or` 在这里用错了！
`score>=80 or score<=89` 这个条件永远成立（所有数字都满足），后面的判断永远跑不到。
**一段区间判断，要用 `and`（并且），不是 or（或者）**

> 
> 80~89：分数大于等于 80 **并且** 小于等于 89 → `score >=80 and score <=89`
记进错题本：
区间判断：**同时满足两个条件用 `and`；满足任意一个条件用 `or`**

```
# D9 + D10 知识点&错题笔记
项目：个人账本（列表+字典嵌套、函数、文件读写、删除功能）

## 一、核心知识点
### 1. 数据结构：列表套字典
适合保存多条结构一样的数据（多条账目）
```python
record_list = [
    {"type":"收入","money":100,"remark":"工资"},
    {"type":"支出","money":20,"remark":"奶茶"}
]
```

- 外层 `list`：可以增、删、循环遍历
- 里面每一项是 `dict`：一条账目，`key` 固定（type、money、remark）
- 取值：`record_list[index]["type"]`

### 2. 函数 def + return

- `def` 定义函数，把一段重复逻辑封装起来
- `return`：把计算结果返回给调用处，**return 会结束函数**，和 print 不一样
  - `print()`：只是打印在终端，数据拿不出来
  - `return`：把值返回，外面变量可以接收结果

```
def calc_balance(record_list):
    # 计算总收入、总支出、余额
    return income, out, bal
```

- 调用：`income, out, bal = calc_balance(record_list)`

### 3. for + enumerate()

`enumerate()` 是 Python 内置函数，循环同时拿到【下标 idx】和【元素 item】

- `idx`：下标（从 0 开始，变量名可以自己改，不是关键字）
- `idx+1`：展示给用户看的序号（人习惯从 1 开始数）

```
for idx, item in enumerate(record_list):
    print(f"{idx+1} | {item['type']} {item['money']}")
```

### 4. 删除元素：del

- `del 列表[下标]`：直接删除指定位置元素，**不会返回被删掉的数据**
- 对比：`列表.pop(下标)` 删除并且返回被删除的数据

> 
> 账本场景不需要拿到删掉的内容，用 del 更合适

```
del record_list[index]
```

### 5. 文件持久化（保存 / 读取）

- `save_records()`：把列表里的账目写入 txt 文件，程序关闭数据不丢失
- `load_records()`：程序启动时，从文件读取账目到列表
- 重点：修改 / 删除账目之后，**必须调用 save_records ()**，不然只改内存，重启程序数据复原

### 6. 输入校验 & 异常捕获 try ... except ValueError

- `ValueError`：值异常。字符串本身是字符串类型，但是内容无法转换成数字（比如输入 abc、汉字）
- 捕获之后，程序不会直接崩溃，给友好提示

```
try:
    num = int(input("输入序号："))
except ValueError:
    print("❌ 请输入合法数字！")
```

### 7. 字符串方法 .strip ()

`字符串.strip()`：去掉字符串前后的空格、换行
用来判断备注是不是空：

```
if remark.strip() == "":
    print("备注不能为空！")
```

### 8. while 菜单循环

`while True` 做主菜单，无限循环，输入 0 执行 break 退出循环

```
while True:
    print("1.新增 2.查看 3.计算余额 4.删除 0.退出")
    choice = input("选择：")
    if choice == "0":
        break
```

### 9. Git 提交要点（配套）

- 流程：`git add 路径/文件名` → `git commit -m "备注"` → `git push`
- 报错 `pathspec ... did not match any files`：文件路径写错，要写相对路径
- `Everything up-to-date`：本地没有新 commit，没有内容可以推送
- 数据文件 account.txt 不要提交，放到 .gitignore 忽略

## 二、高频错题 & 踩坑记录

1. **下标坑**：用户输入序号是 1、2、3，程序列表下标从 0 开始，要 `index = num - 1`
2. **缩进坑**：Python 缩进决定代码归属，缩进错，变量作用域出错（NameError）
3. **删除后忘记 save**：内存删了，文件没更新，重启账目又回来
4. **区分 idx 和 item**：idx 是下标位置，item 是单条账目字典；idx 只是自定义变量名，不是关键字
5. **print 和 return 混淆**：函数只用 print，外面拿不到计算结果
6. **try-except 范围**：只捕获转数字那一行，不要把全部逻辑包进去
7. **Git 找不到文件**：add 的时候要写完整相对路径，不能只写文件名

## 三、账本功能清单（D9+D10 完成）

✅ 新增收支（备注判空、金额数字校验）
✅ 查看全部账目（带序号 enumerate）
✅ 自动计算：总收入、总支出、余额
✅ 删除账目（序号选择 + y/n 确认防误删 + 异常捕获 + 自动保存）
✅ 数据持久化：写入 txt，重启加载
✅ 菜单循环，输入错误友好提示

## 四、概念简答自测（口述）

1. print 和 return 的区别？
2. enumerate 作用是什么？idx 是什么？
3. del 和 pop 的区别？
4. ValueError 什么时候触发？
5. 为什么删除账目之后要调用 save_records？
### 1. print 和 return 的区别

- `print()`：只是**在控制台打印文字**，仅用来给人看，不会把数据交给外面的代码；函数外部拿不到这个值。
- `return`：把数据**返回给调用这个函数的地方**，数据可以存到变量里继续使用；`return` 执行后会直接结束函数。

> 
> 一句话：print 是展示，return 是传回数据。

### 2. enumerate 作用是什么？idx 是什么？

- `enumerate()`：循环的时候，可以**同时拿到下标和对应的元素**，不用自己单独定义计数器。
- `idx`：就是当前元素的下标，从 0 开始；是我们自己取的变量名，不是关键字。

> 
> 账本里 `idx+1`，就是给用户展示从 1 开始的序号。

### 3. del 和 pop 的区别

- `del 列表[下标]`：删除指定位置元素，**不返回被删掉的数据**。
- `列表.pop(下标)`：删除指定位置元素，**同时把删掉的这条数据返回出来**，可以用变量接住。

> 
> 咱们删除账目不需要拿到删掉的记录，用 del 更合适。

### 4. ValueError 什么时候触发？

值异常：**数据类型是对的（字符串），但是内容不能做对应转换**。
典型场景：`int("abc")`、`float("哈哈")`，输入的文字没法转成数字，就抛出这个报错，我们用 try except 捕获它，防止程序崩溃。

### 5. 为什么删除账目之后要调用 save_records？

我们修改、删除的内容一开始只在**内存里**，内存的数据程序一关就消失。
`save_records()` 会把最新的账目列表写入 txt 文件，做持久化保存；如果不调用，重启程序，删掉的账目又会从文件读回来。

1. with 上下文管理器打开文件，自动 close，防止资源泄露
2. w 覆盖、a 追加，账本用 w 全量重写
3. FileNotFoundError：读取不存在的文件触发

**JSON 是干什么的？**
JSON 是一种通用文本格式，专门用来存**字典、列表这类结构化数据**，可以直接保存嵌套数据，不用自己手动写分隔符，不会出现上面逗号冲突的问题。

**序列化、反序列化**

- **序列化**：Python 里的列表 / 字典（内存里的对象）→ 转成 JSON 字符串，写入文件保存
- **反序列化**：读取文件里的 JSON 字符串 → 转回 Python 列表 / 字典，程序直接拿来用

JSONDecodeError：专门用来捕获 json 文件内容错乱（比如手动改乱文件、乱加符号）

## error_book.md 新增条目（D12）
### 报错1：UnboundLocalError
**现象**：cannot access local variable 'xxx' where it is not associated with a value
**原因**：函数内分支不全，部分执行路径下变量没有赋值，执行return/使用变量的时候，变量不存在。
**本次踩坑场景**：try里面写`date = json.load(f)`，except分支赋值`data = []`，return写`date`；异常分支里date没有定义，直接报错。
**解决**：保证所有分支路径，变量都有初始值，变量名全程统一，不要拼写混用。

### 报错2：NameError: name 'xxx' is not defined
**现象**：调用函数的时候提示名字未定义
**原因**：Python从上往下顺序执行代码，函数调用写在了def函数定义的前面。
**解决**：先写def定义函数，再在下方调用这个函数。

### 报错3：json.JSONDecodeError
**现象**：JSON文件格式损坏、内容非法，json.load()解析失败
**原因**：文件里面不是合法JSON结构
**解决**：增加except捕获这个异常，兜底返回空列表，程序不崩溃。

### 报错4：FileNotFoundError
**现象**：打开的文件不存在
**解决**：捕获异常，返回空账本，自动新建保存。

### 报错5：git push Recv failure: Connection was reset
**现象**：推送GitHub时报连接被重置
**原因**：本地到GitHub网络波动/网络不通
**解决**：commit已经成功，改动保存在本地；重试push，或者切换热点再推送。

### 其他非报错坑点
1. 多处调用load_records()，会重复打印加载提示，也重复读文件；优化：程序启动只加载一次，把账本数据存在record_list，增删改之后只save_records保存，不再重复load。
2. 文件写入模式混淆：账本不能用a追加，要用w覆盖写入，防止账目重复叠加。

## D12 今日报错总结（error_book 用）

### 一、导入类报错：ImportError

**现象**：`cannot import name 'xxx' from 'storage/ledger'`
**根因**：main.py 里导入的函数名，和模块里 `def` 定义的名字对不上。

- 单复数不一致：`load_record` ↔ `load_records`、`xiugai_record` ↔ `xiugai_records`
- 拼写不一致：导入名和定义名差一个字母
**修复**：两边命名统一，推荐都用复数 `records`；保存文件后重新运行。
**教训**：导入语句必须逐字母核对，函数名、单复数完全一致。

### 二、未定义变量报错：NameError / UnboundLocalError

**现象 1**：`NameError: name 'record_list' is not defined`
**根因**：`delete_record` 里调用 `show_all()` 漏传参数，函数内拿不到列表。
**修复**：`show_all(record_list)`，把形参传进去。

**现象 2**：`UnboundLocalError: cannot access local variable 'r_type' ...`
**根因**：三层 while 输入校验缩进错乱，`r_type` 未被成功赋值就传到 `add_record`。
**修复**：收支类型、金额、备注三段校验全部在 `if choice == "1":` 内部；只有三项全部校验通过，才执行新增函数。

**现象 3**：变量名拼写错误 `recordf_list`（多打字母 f）
**根因**：Python 区分变量名，`record_list` 和 `recordf_list` 是两个不同变量。
**修复**：统一改回 `record_list`。

### 三、分层与持久化逻辑问题（不崩溃，但功能失效）

**现象**：删除 / 修改后，重启程序数据又回来了，"没有保存"。
**根因**：

1. ledger 业务层函数里直接调用 `save_records`，重复写文件、违反分层；
2. 函数没有 `return True/False`，main 拿不到改动标记；
3. main 里只写了 `changed = delete_record(...)`，**缺 `if changed:` 判断和 `save_records(record_list)`**。
**修复**：

- ledger 只操作列表，成功返回 `True`，失败 / 取消返回 `False`，不碰文件读写；
- main 接收返回值，只有 `changed` 为 True 时才调用保存。

### 四、今日踩坑清单（记错题本）

表格

| 序号 | 报错类型 | 一句话原因 |
| --- | --- | --- |
| 1 | ImportError | 导入名与 def 定义名不一致（单复数 / 拼写） |
| 2 | NameError | 调用函数漏传形参 |
| 3 | UnboundLocalError | 输入校验缩进错乱，变量未赋值就使用 |
| 4 | 变量拼写 | 手误多打字母，导致变量名不一致 |
| 5 | 数据不持久化 | 拿到 changed 标记后漏判断、漏调用 save_records |

### 五、规范复盘

- **storage.py**：只负责 JSON 读写；
- **ledger.py**：只操作列表，return 布尔值，不直接保存文件；
- **main.py**：交互入口，依据返回值决定是否持久化。

## D14 错题记录（JSON 容错重构）

### 报错1：TypeError: 'NoneType' object is not iterable
- 报错原文：`TypeError: 'NoneType' object is not iterable`
- 原因分析：JSON 损坏分支返回 `None`，main 里判断 `record_list is None` 后没有 `exit()` 阻断，代码继续进入菜单，把 `None` 传给 `show_all` 做 for 循环遍历
- 正确写法：检测到 `None` 立刻 `exit()` 终止后续代码；D14 重构后损坏分支改为备份文件并返回空列表，不再返回 `None`
- 关联知识点：异常分支返回值、变量作用域、for 遍历对象必须是可迭代类型

### 报错2：清理脏数据时把全部数据清空
- 现象：执行脏数据清理后，账本所有正常记录一起消失
- 原因分析：`JSONDecodeError` 分支直接返回空列表，随后触发自动 `save_records` 覆盖写入；或校验条件里 key 名和 JSON 字段对不上（如 `type` vs `r_type`），合法记录被全部误判为脏数据
- 正确写法：文件损坏时禁止直接覆盖写入；校验 key 名必须与 JSON 字段一致；清理前先逐条打印确认哪些记录被判脏
- 关联知识点：脏数据逐条过滤、文件备份策略、数据安全兜底

### 报错3：解包报错 not enough values to unpack
- 报错原文：`ValueError: not enough values to unpack (expected 2, got 1)`
- 原因分析：`load_records` 各异常分支 return 的值个数不一致，有的只返回列表，有的返回 `(列表, 脏数据条数)`，main 解包时数量对不上
- 正确写法：所有出口统一返回成对的 `(record_list, dirty_count)`
- 关联知识点：函数多返回值、元组解包

### 非报错坑点
1. `os` 模块必须先 `import os`，否则 `os.rename` 报 `NameError`；`json` 模块管 JSON 解析，`os` 模块管文件改名/路径操作。
2. 损坏文件先 `.bak` 备份再重建空账本，不能直接删除覆盖，防止误删可恢复的历史数据。

## D15 排错记录：程序启动读不到文件里的账单

### 报错1：NameError，模块顶层残留调试代码
- 报错原文：`NameError: name 'data' is not defined`（导入 storage 时直接崩溃）
- 原因分析：调试用的 `print(data)`、`print(valid_list)` 写在了函数外面的模块顶层，`import storage` 时立刻执行，但 `data`、`valid_list` 从未定义
- 正确写法：临时调试打印必须放在函数内部；调试完删除，不要留在模块顶层
- 关联知识点：模块导入即执行顶层代码、变量作用域

### 报错2：校验循环漏 append，且 return 写在 for 内部
- 现象：文件 JSON 合法、记录正常，但加载出来列表永远是空的
- 原因分析：遍历 `raw_list` 时，合法记录没有 `record_list.append(item)`；`return record_list, dirty_count` 写在 for 循环体内，第一条处理完就提前返回，后面记录不再遍历
- 正确写法：`continue` 跳过脏数据，合法记录 `append` 进列表；`return` 必须放在 for 循环外面，全部遍历完再统一返回
- 关联知识点：循环结构、函数返回时机、列表增删

### 报错3：相对路径与运行目录不一致，找不到 account.json
- 现象：代码在 `day01\week1\`，数据文件在项目根目录；从 week1 目录运行时，相对路径 `open("account.json")` 找不到文件，走 `FileNotFoundError` 返回空账本
- 原因分析：相对路径依赖运行时的当前工作目录（cwd），代码文件和数据文件不在同一目录时就会找不到
- 正确写法：用 `os.path.abspath(__file__)` 基于脚本自身位置逐级向上定位数据文件，不依赖 cwd；`os.path.exists` 先判断
- 关联知识点：绝对路径/相对路径、`__file__`、os.path 模块

### 报错4：形参拼写 recordf_list
- 现象：`calc_balance(recordf_list)` 形参名多打字母 f，内部循环也跟着用这个错名
- 原因分析：手误拼写，Python 把它当成另一个变量名；内部自洽时不报错，但可读性差、易引发后续 NameError
- 正确写法：统一改回 `record_list`，变量名见名知义
- 关联知识点：命名规范、变量拼写一致性