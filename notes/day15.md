### 今日目标

把账本函数写成规范、可复用、可讲解的形式：掌握位置参数、默认参数、关键字参数，理解多返回值与变量作用域，给全部函数补上 docstring 文档字符串。

### 核心知识点

1. **三种传参方式**
   - **位置参数**：按定义顺序传参，顺序不能乱，必填参数放在前面。
   - **默认参数**：定义时给默认值，调用时可以省略不传；默认参数必须写在位置参数后面。
   - **关键字参数**：调用时写 `参数名=值`，顺序可以随意调换，可读性强。

2. **多返回值**
   - `return income, outlay, balance` 本质返回的是一个**元组（tuple）**，不是列表。
   - 接收时按位置解包：`a, b, c = func()`。
   - 解包数量不一致会报 `ValueError`：值多个变量少是 `too many values to unpack`；值少个变量多是 `not enough values to unpack`。

3. **变量作用域**
   - **局部变量**：函数内部定义，只在该函数内可用，出了函数访问不到。
   - **全局变量**：函数外部定义；函数内部默认只能读，要修改必须先 `global` 声明。
   - 账本里优先用参数在函数间传递列表，不靠全局变量共享：作用域清晰、避免意外覆盖、函数可复用可测试、符合分层规范。

4. **docstring 文档字符串**
   - 位置：紧跟 `def 函数名(...)` 冒号的下一行，用三引号 `""" """` 包裹，是函数定义的第一句。
   - 作用：写清功能、参数、返回值；属于函数对象的一部分，`help(函数名)` 可以读取出来。
   - 区别：`#` 是普通行注释，解释器直接忽略，只给人看；docstring 属于函数本身，程序能拿到这段说明。
   - 约定：「参数」只写 `def` 括号里的形参；函数内部 input 收取的局部变量、`return` 出去的值，分别放在返回段，不要混进参数段。

### 关键代码片段

```python
# 默认参数示例：tax 有默认值 0，放在位置参数后面
def calc_balance(record_list, tax=0):
    """计算总收入、总支出和余额。

    参数:
        record_list: list，账目列表
        tax: float，税率，默认 0，本次练习暂不参与余额计算
    返回:
        tuple: (总收入, 总支出, 余额)
    """
    total_zongshouru = 0
    total_zongzhichu = 0
    for item in record_list:
        if item["r_type"] == "收入":
            total_zongshouru += item["money"]
        elif item["r_type"] == "支出":
            total_zongzhichu += item["money"]
    balance = total_zongshouru - total_zongzhichu
    return total_zongshouru, total_zongzhichu, balance
```

```python
# 调用：不传 tax 用默认 0；也可以用关键字参数显式指定
zongshouru, zongzhichu, bal = calc_balance(record_list)
zongshouru, zongzhichu, bal = calc_balance(record_list, tax=0.13)
```

```python
# docstring 模板
def add_record(record_list, r_type, money, remark):
    """新增一条账目记录。

    参数:
        record_list: list，存储所有账目的列表
        r_type: str，收支类型，"收入"或"支出"
        money: float，账目的金额
        remark: str，账目备注信息
    返回:
        bool: True 代表添加成功
    """
```

### 口述自测题与标准答案

**1. 位置参数、默认参数、关键字参数有什么区别？**

答：位置参数按定义顺序传，顺序不能乱，必填在前；默认参数定义时给默认值，调用可省略，且必须写在位置参数后面；关键字参数调用时 `参数名=值`，顺序可换，可读性强。

**2. `return x, y` 返回的是列表还是元组？解包数量不一致会报什么错误？**

答：返回的是元组（tuple）。解包变量个数和返回值个数不一致会报 `ValueError`：值多个变量少是 `too many values to unpack`，值少个变量多是 `not enough values to unpack`。

**3. 局部变量和全局变量有什么区别？账本为什么优先用参数传递而不用全局变量？**

答：局部变量在函数内部定义，仅函数内可用；全局变量在函数外部定义，函数内默认只读，修改需要 `global` 声明。账本优先参数传递是因为作用域清晰、避免多个函数意外覆盖同一份数据、函数可复用可测试，也符合 main 持有列表、ledger 只接收处理的分层规范。

**4. docstring 写在哪里，起什么作用？**

答：紧跟 `def` 下一行，用三引号包裹。作用是说明功能、参数、返回值；它属于函数对象本身，`help()` 可以读取；区别于被解释器忽略的 `#` 行注释。

### 今日踩坑（同步 error_book.md）

- docstring 的「参数」段只写形参，不要把函数内部 input 收的局部变量、返回值误写进参数段。
- 文档写了某个参数，`def` 括号里必须有对应形参，保持文档和代码一致（`tax` 案例）。
- 函数返回 `bool` 就不能在 docstring 里写成 `None`，返回说明要和真实 return 一致。

### 明日待办

- [ ] 通读三个文件，确认增删改查、JSON 容错、脏数据过滤全部正常
- [ ] Git 提交：`D15 函数进阶，补全docstring，练习默认参数`
- [ ] 预习 D16：模块与包、import 原理、pip 与 requirements.txt
