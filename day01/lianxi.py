## 题目 1（基础）
#遍历这两个列表，打印每一个人的名字 + 分数，格式示例：`张三：92分`
## 题目 2（查找，必练 flag）
#输入一个完整姓名，程序去循环查找：
#- 找到：打印这个人的分数
#- 找不到：只打印一次「没有找到该学生」
## 题目 3（按姓氏查找，今天重点）
#输入一个姓氏，把所有这个姓氏的学生全部打印出来；没有就提示「没有这个姓氏的学生」
## 题目 4（拓展，结合之前 if 分级）
#在题目 3 基础上，查到学生之后，额外输出评级：
#- ≥90：优秀
#- 80~89：良好
#- 60~79：及格
#- <60：不及格
## 题目 1（基础）
#遍历这两个列表，打印每一个人的名字 + 分数，格式示例：`张三：92分`
name_list = ["张三","李四","王五","赵六","张小花","李磊"]
score_list = [92, 55, 78, 83, 67, 89]
for i in range(len(name_list)):
    print(f'{name_list[i]}的分数：{score_list[i]}')


## 题目 2（查找，必练 flag）
#输入一个完整姓名，程序去循环查找：
#- 找到：打印这个人的分数
#- 找不到：只打印一次「没有找到该学生」
name_list = ["张三","李四","王五","赵六","张小花","李磊"]
score_list = [92, 55, 78, 83, 67, 89]
input_name=input('请输入名字：')
for i in range(len(name_list)):
    if name_list[i]==input_name:
        print(f'{input_name}的分数是：{score_list[i]}')
        break  # 找到就跳出循环，不用继续找了
else:
    print('查无此人')
#在题目 3 基础上，查到学生之后，额外输出评级：
#- ≥90：优秀
#- 80~89：良好
#- 60~79：及格
#- <60：不及格
name_list = ["张三","李四","王五","赵六","张小花","李磊"]
score_list = [92, 55, 78, 83, 67, 89]
input_xing=input('请输入姓氏：')
has_find=False
for i in range(len(name_list)):
    name=name_list[i]
    score=score_list[i]
    if name[0]==input_xing:
        has_find=True
        if score<60:
            level = "不及格"
        elif score<80:
            level = "及格"
        elif score<90:
            level = "良好"
        else:
            level = "优秀"
        print(f'{name}:{score}分,评级:{level}')
        break
if not has_find:
    print('未查到此人！')
            
#在题目 4 基础上，查到学生之后，额外输出评级：
#- ≥90：优秀
#- 80~89：良好
#- 60~79：及格
#- <60：不及格
name_list = ["张三","李四","王五","赵六","张小花","李磊"]
score_list = [92, 55, 78, 83, 67, 89]
for i in range(len(name_list)):
    name=name_list[i]
    score=score_list[i]
    if score<60:
        level = "不及格"
    elif score<80:
        level = "及格"
    elif score<90:
        level = "良好"
    else:
        level = "优秀"
    print(f'{name}:{score}分,评级:{level}')