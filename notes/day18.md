### 今日目标
看懂提交历史，学会查看历史改动；区分两种回滚方式；掌握分支合并 merge；理解冲突产生场景。

### 常用命令速查
| 命令 | 作用 |
|---|---|
| git log | 完整提交日志 |
| git log --oneline | 简洁短哈希日志，每条一行（高频） |
| git show 短哈希 | 查看某一次提交的完整文件改动详情 |
| git switch main | 切到接收代码的目标分支 |
| git merge 来源分支 | 把来源分支合并进当前所在分支 |
| git branch -d 分支名 | 安全删除已合并完毕的本地分支 |
| git checkout 哈希 -- 文件名 | 只恢复单个文件到历史版本 |
| git reset --hard 哈希 | 整个仓库强制回退到某快照，丢弃后面所有提交 |
| git merge --abort | 放弃本次合并，恢复合并前状态 |

### merge 实操记录
- 合并前先切到目标分支：git switch main
- 执行合并：git merge dev-d17
- 合并结果：Fast-forward（快进合并，无冲突），main 分支拿到 notes/day17.md
- 合并后删除练习分支：git branch -d dev-d17
- 推送远程：git push origin main

### 冲突说明
- 冲突原因：同一个文件的同一行，在两个分支做了不一样的修改，Git 分不清保留哪一份。
- 处理方式：手动打开文件，删掉 `<<<<<<<` `=======` `>>>>>>>` 标记，编辑保存后 add + commit 完成合并。

### 两种回滚对比
| 方式 | 作用范围 | 是否改动提交历史 | 风险 |
|---|---|---|---|
| git checkout 哈希 -- 文件 | 只恢复单个文件 | 不改动整体提交链 | 安全 |
| git reset --hard 哈希 | 整个仓库回退 | 丢弃该哈希之后所有提交 | 危险，已推送远程的分支慎用 |

### 口述自测（自己写答案）
1. git show 的作用是什么？
2. merge 合并分支前，为什么要先切换到 main？
3. Git 冲突是什么情况下产生？
4. git checkout 哈希 -- 文件 和 git reset --hard 哈希 的区别，哪个更危险？

### 踩坑记录
- 哈希值输错（多打字母）会报 `ambiguous argument: unknown revision`，短哈希取前 6-7 位即可，对照日志仔细核对。
- 本地存在未跟踪同名文件时，merge 会被拒绝（untracked working tree files would be overwritten），先删除或备份该文件再合并。
- 进入日志分页界面后，按 q 退出。
