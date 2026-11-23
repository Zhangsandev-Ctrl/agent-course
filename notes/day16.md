### 今日目标

理解 Python 模块拆分机制和依赖管理：把可复用的工具函数抽到独立 `utils.py`，理清 import 方向、避免循环导入，整理 `requirements.txt` 和 `.gitignore`。

### 核心知识点

1. **模块（module）**
   一个 `.py` 文件就是一个模块。模块名 = 文件名去掉 `.py` 后缀（`storage.py` → `storage`），import 时按这个名字找同目录文件，名字必须逐字母一致。

2. **两种 import 写法**
   - `import 模块名`：导入整个模块，调用时带前缀 `模块名.函数名()`，如 `json.load(f)`。
   - `from 模块名 import 函数名`：只导入指定函数，调用时直接用函数名，不带前缀。
   - `json`、`os` 是 Python 自带标准库；`storage`、`ledger`、`utils` 是本地模块，import 机制相同。

3. **循环导入**
   两个模块互相 import 对方形成闭环，Python 从上往下加载时一方还没加载完，就会报 `ImportError`。
   依赖保持单向：`main` → `storage / ledger / utils`，底层模块不反向依赖上层；需要共享的逻辑抽到独立 `utils.py`。

4. **pip 与 requirements.txt**
   - `pip install 包名`：安装第三方库；`pip list`：查看已装包。
   - `requirements.txt`：记录项目用到的第三方库及版本，别人拿到项目用 `pip install -r requirements.txt` 一键装环境。
   - 标准库 `json/os` 自带，不写入 requirements。
   - 虚拟环境 `venv`：不同项目依赖互不干扰（先看懂概念）。

5. **.gitignore**
   告诉 Git 哪些文件不提交：缓存（`__pycache__/`、`*.pyc`）、虚拟环境（`.venv/`）、密钥敏感文件（`.env`）、个人编辑器配置（`.idea/`）、系统垃圾（`.DS_Store`）。源码和配置清单要提交，缓存/环境/密钥不提交。

### 关键代码片段

```python
# utils.py：可复用的工具函数，不依赖账本业务
def is_valid_money(value):
    """判断金额是否为合法正数（排除 bool）。"""
    return isinstance(value, (int, float)) and not isinstance(value, bool) and value > 0
```

```python
# ledger.py / main.py 单向导入底层模块
from utils import is_valid_money
```

```python
# 金额校验：转换归交互层，合法性判断交给工具函数
while True:
    try:
        new_money = float(input("请输入金额：").strip())
    except ValueError:
        print("❌ 金额必须是数字！")
        continue
    if not is_valid_money(new_money):
        print("❌ 金额必须大于0！")
        continue
    break
```

### 口述自测题与标准答案

**1. 什么是模块？模块名和文件名是什么关系？**

答：一个 `.py` 文件就是一个模块；模块名是文件名去掉 `.py` 后缀，import 时按这个名字找同目录文件，必须逐字母一致。

**2. `import json` 和 `from storage import load_records` 两种写法有什么区别？**

答：`import 模块名` 导入整个模块，调用要带前缀 `模块名.函数名()`；`from 模块名 import 函数名` 只导入指定函数，直接用函数名调用，不带前缀。

**3. 什么是循环导入？为什么 storage 和 ledger 不能互相导入？**

答：两个模块互相 import 对方形成闭环，加载时一方还没加载完，会报 ImportError。storage 管文件、ledger 管业务，职责分开；数据靠参数传递，不需要互相依赖；共享逻辑抽到 utils.py，保持单向依赖。

**4. requirements.txt 是干什么用的？标准库 json/os 要不要写进去？**

答：记录项目用到的第三方库和版本，别人用 `pip install -r requirements.txt` 一键装环境。标准库 Python 自带，不需要安装，不写进去。

**5. .gitignore 通常忽略哪些东西？**

答：缓存（`__pycache__/`、`*.pyc`）、虚拟环境（`.venv/`）、密钥敏感文件（`.env`）、个人编辑器配置（`.idea/`）、系统垃圾（`.DS_Store`）；源码和配置清单提交，其余不提交。

### 今日踩坑（同步 error_book.md）

- 新建模块文件后要先保存到磁盘，否则文件 0 字节、导入找不到函数。
- 函数体必须缩进进 `def` 内部，否则 `IndentationError`。
- 调用工具函数时变量名要和当前函数作用域一致（`new_money` 不能写成 `money`）。
- 校验分支：非法 → `print + continue`，合法 → `break`，顺序不能反。

### 明日待办

- [ ] 通读四个文件，确认单向依赖、增删改查与 JSON 容错正常
- [ ] Git 提交：`D16 模块拆分与依赖管理，抽取utils工具模块，整理requirements与gitignore`
- [ ] 预习 D17：Git 基础操作复盘、commit 规范、分支概念
