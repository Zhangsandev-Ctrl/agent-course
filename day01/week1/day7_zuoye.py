# D6 独立作业 day6_while.py

#需求：

#1. 用 while 循环实现：让用户不断输入学生名字，输入 `q` 的时候停止录入
#2. 每录入一个名字，就存进列表 name_list
#3. 结束之后，打印全部录入的学生名单
#提示：

#- 先创建空列表 `name_list = []`
#- 循环里用 `input()` 获取输入
#- 判断如果输入等于 `"q"`，就 `break`
#- 不是 q，就用 `.append()` 添加到列表
name_list = []# 1. 先建一个空列表，用来放名字
# 2. while 循环，条件写 True 代表无限循环，需要靠break退出
while True:
    name=input('请输入学生名字,输入q结束录入:')# 3. 获取用户输入
    if name =='q':# 4. 判断：如果输入的是q，就break跳出循环
        break
    name_list.append(name)# 5. 不是q，就把名字加到列表里面
print('全部学生名单：',name_list)# 6. 循环结束之后，打印全部名单
#**同时录入名字和分数**

#1. 两个空列表：`name_list = []`、`score_list = []`
#2. while 循环，先输入名字；名字输入`q`，直接结束
#3. 名字不是 q，再输入分数（注意：`input拿到的是字符串，要用int()`转成数字）
#4. 名字 append 进 name_list，分数 append 进 score_list
#5. 结束之后，循环打印：名字 + 分数
name_list = []
score_list = []
while True:
    name=input('请输入学生名字：')
    if name=='q':
        break
        score=input('请输入学生分数：')
        score=int(score)
    name_list.append(name)
    score_list.append(score)
for i in range(len(name_list)):
    print(name_list[i],score_list[i])