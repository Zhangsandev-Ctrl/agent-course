#新增学习：`isdigit()`（字符串方法）:只判断**纯正数字字符串**；负数、小数返回 False;只能字符串调用，数字变量不能用 `.isdigit()`
#1. `isdigit()` **只认全部是 0-9 的字符串**，才返回 True
#2. 只要里面有 `.` 小数点、`-` 负号、字母，一律返回 False
#3. 它只适合校验**正整数输入**，小数、负数它判断不了
#4. 必须是字符串（带引号）才能调用，int 数字直接调用会报错

stu={'name':'张三','score':'88','age':'17'}
print(stu['name'])
print(stu['score'])
stu['score']
stu["gender"]='男'
print(stu)
for k,v in stu.items():
    print(k,v)
#print(stu['phone'])

#1. 定义字典，保存学生信息：`name、score、age、city`
#2. 用 `.items()` 循环遍历，打印全部键和值
#3. 修改他的分数；新增一对键值对 `hobby`（爱好）
#4. 打印修改之后完整的字典
#5. 额外测试：`stu[0]` 用数字下标取值，观察报错
stu1={'name':'李四','score':'90','age':'18','city':'洛阳'}
print(stu1['name'])
print(stu1['score'])
stu1['score']
stu1['hobby']='游戏'
print(stu1)
for k,v in stu1.items():
    print(k,v)
## 题目：学生成绩查询系统

#需求：
#1. 预先用**字典**存多名学生信息，外面套列表（列表嵌套字典）
#student_list = [
   # {"name":"张三", "score":85},
   # {"name":"李四", "score":92},
   # {"name":"王五", "score":76}


#2. 循环：让用户输入学生名字来查询分数，输入 `q` 就退出程序
#3. 校验规则：
   #- 如果名字存在：打印「xxx 的分数是：xx」，同时判断等级：≥90 优秀，≥80 良好，≥60 及格，<60 不及格
   #- 如果名字不存在：提示「没有找到该学生」
#4. 额外要求：用 while 做循环，不能直接写死查询次数
#5. 拓展加分项（可选）：如果用户输入空内容，提示不能输入空白，重新输入
student_list=[{"name":"张三", "score":85}, 
              {"name":"李四", "score":92},
              {"name":"王五", "score":76}]
while True:
    name_input=input('请输入学生名字输入q退出:')
    if name_input.strip() == "":
        print("不能输入空白，请重新输入！")
        continue
    if name_input=='q':
        break
   #- 如果名字不存在：提示「没有找到该学生」
    found = False # 标记变量，一开始默认没找到
    for stu2 in student_list:
        if stu2['name']==name_input:
            found=True
            score=stu2['score']
            if score < 60:
                level='不及格'
            elif score<79:
                level='及格'
            elif score<90:
                level='良好'
            else:
                level='优秀'
            print(f'{stu2["name"]}的分数为{stu2["score"]}分,评级：{level}')
            break
    if not found:
        print('没有找到该学生')
## 题目：学生成绩录入 & 统计系统
#需求：
#1. 初始是空列表 `student_list = []`，用来存学生字典 `{"name":"xxx", "score":xx}`
#2. while 循环，菜单选择：
   #- 输入 `1`：新增学生，先输入名字，再输入分数
   #- 输入 `2`：查看全部学生 + 统计总分、平均分
   #- 输入 `3`：退出程序
#3. 校验规则（重点）
   #- 名字不能是空（直接回车要拦截，提示重新输入）
   #- 分数必须是数字，用 `isdigit()` 判断；不是数字就提示无效，重新输入分数
   #- 分数范围 0~100，超出范围提示分数不合法，重新输入
#4. 加分要求：录入的时候，**不能录入同名学生**，如果名字已经存在，提示 “该学生已存在，不能重复添加”
