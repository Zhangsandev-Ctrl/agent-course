## 基础题（1、2，巩固 print + 变量）

#1. 定义变量 `name` 存你的名字，变量 `age` 存你的年龄，用 print 打印一句话：`我叫XXX，今年XX岁`
#2. 定义两个变量 a=10，b=20，用 print 分别打印 a+b 的结果、a-b 的结果

# 第1题：名字+年龄
name = "张同学"
age = 18
print("你好，我叫", name, "今年", age, "岁")

# 第2题：a b 加减计算
a = 10
b = 20
print("a + b =", a + b)
print("a - b =", a - b)
## 进阶题（3、4，自定义函数 def）

#3. 写一个函数 `say_hello()`，函数内部用 print 输出 `欢迎学习Agent开发`，调用这个函数，让程序运行时打印这句话
#4. 写函数 `calc_sum()`，里面设置 x=6，y=7，打印 x+y 的结果；调用函数
#第3题：调用函数
#def say_hello():
    #print("欢迎学习Agent开发")
#say_hello()
#第4题：写函数 `calc_sum()`，里面设置 x=6，y=7，打印 x+y 的结果；调用函数
#def calc_sum():
    x=6
    y=7
    #print(x+y)
#calc_sum()
## 拔高题（5，if 分支，融合前面所有知识点）

#5. 定义变量 score，赋值为 75，写判断逻辑：
score=59
if score>100 or score<0:
    print("报错提示：输入有误请重新输入")
elif score>=90:
    print("优秀")
elif score>=80:
    print("良好")
elif score>=60:
    print("及格")
else :
    print("不及格")
#附加思考题第 6 题（多分支，融合前面所有知识点）改造第 5 题，升级多分支：> =90 → 优秀; > =80 → 良好;>=60 及格 ；<60 不及格

