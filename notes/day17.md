### 今日目标
复盘 Git 基础命令，理解工作区/暂存区/仓库三个区域与分支概念，养成规范提交习惯。

### 常用命令速查
| 命令 | 作用 |
|---|---|
| git status | 查看改动、暂存状态、当前分支 |
| git add 文件名 | 单文件进暂存区；git add . 全部进暂存区 |
| git commit -m "说明" | 暂存区快照存成本地提交 |
| git log --oneline | 历史提交，每条一行 |
| git diff | 未 add 的改动对比 |
| git diff --cached | 已 add 未 commit 的改动对比 |
| git branch | 查看分支，* 标当前分支 |
| git branch 分支名 | 新建分支 |
| git checkout 分支名 | 切换分支（新写法 git switch） |

### commit message 规范
格式：<类型>: <做了什么>
- feat 新功能 / fix 修 bug / refactor 重构不改功能 / docs 文档笔记 / chore 配置依赖
- 反面教材：更新代码、改了点东西、fix、测试、111
- 旧历史不要用 --amend / rebase 改，只写规范对照

### 旧提交规范对照（自己填 2 条）
| 旧 message | 规范改写 |
|---|---|
|  |  |

### 分支练习记录
- 新建分支：
- 切换分支：
- 分支上做了什么：
- 切回 main：

### 口述自测（自己写答案）
1. add 和 commit 各管什么？跳过 add 直接 commit 会怎样？
2. git diff 和 git diff --cached 区别？
3. 什么是分支？为什么不直接在 main 上改？
4. git log --oneline 里短哈希干什么用？
5. .gitignore 要不要写标准库？要不要写 .env？
