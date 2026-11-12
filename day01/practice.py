# 1. 变量：就是给一个值起名字，方便后面反复用
#name = "张同学"

#age = 25

# 2. print:把内容显示到屏幕上
#print("你好","我叫",name)

# 3. 简单计算
#next_year_age = age + 1
#print("明年我",next_year_age,"岁")

# 4. function（函数）：把一段动作打包，起个名字，随时调用
#def introduce():
    #print("我在学agent开发,目标1个月就业")


#introduce()


#name = "孟小狗"
#age = 26
#print("你好","我叫",name)
#next_year_age = age + 1
#print("明年我",next_year_age,"岁")

#def introduce():
    #print("我在学习AGENT开发,目标1个月就业")
#introduce()

#jintian="第一天!加油~"
#print(jintian)
#def xuexijilu():
    #print("今天学习了def定义函数,print为python内置函数意思为打印输出,薄弱点英语差,应用能力不行")
#xuexijilu()

#name = "张同学"#名字
#age = 26#年龄
#height = 1.82#身高
#is_student = False#真假 `bool`（True/False 首字母大写）
#score = 72#成绩
#if score >= 60:
    #print("及格")
#else:
    #print("不及格")
#if is_student :
    #text = "是"
#else:
    #text = "不是"#新手版
#text = "是" if is_student else "不是"#简化版
#print(f"你好,我叫{name},今年{age}岁,身高{height}米,我{text}学生,我考了{score}分")
#print(type(name),type(age),type(height),type(is_student))

#day3
#	本周踩过的坑（错题本条目）	重做验证动作（自己敲，不许照抄截图）	合格标准
#1	def 定义函数后忘记调用	重写 say_hello() 定义 + 单独一行调用并运行	不调用时无输出，调用后打印成功，能讲清 "定义≠执行"
#2	= 赋值 和 == 判断相等混淆	写 a=5、再写 print(a==5)、print(a!=5) 各一次	说得出：= 装值，== 问是否相等，!= 问是否不等，结果 True/False
#3	if/elif/else 行末漏英文冒号（报过 SyntaxError: expected ':'）	故意先不写冒号运行看报错，再补冒号重跑	能说出冒号必须英文、后跟缩进
#4	缩进混乱	在 if 内、外各放一条 print，观察谁受条件控制	能讲清 Python 用缩进划分归属，缩进错 = 逻辑错
#5	区间判断误用 or（score>=80 or score<=89 恒成立）	改成区间写法并说出为什么区间要用 and	75、85、95 三个值分别落到及格 / 良好 / 优秀
#6	elif 分支顺序写乱（低分判断跑到前面拦截）	按 优秀→良好→及格→不及格 从高到低重排	60 分判 "及格" 不判 "不及格"，顺序调换会出错并能解释原因
#7	文字没加英文引号（裸写我叫被当变量）	写两条 print：一条文字带引号、一条不带，对比报错	说清字符串必须 "英文引号" 包裹
#8	同名变量被二次赋值覆盖（age=b-a 冲掉年龄）	把 "个人信息" 和 "计算结果" 用不同变量名分开写	自我介绍打印出真实年龄，不被计算值覆盖
#9	True/False 必须首字母大写；布尔可直接进 if	写 if is_student: 与 if is_student==True: 对比	能说明两者等价、小写 true 会报错
#10	f-string：f"我叫{name}，今年{age}岁"	把变量填进一句话打印	花括号里是变量名，外面是普通文字
#1
def say_hello():
    print("定义函数：定义不等于调用，不调用时无输出")
say_hello()

#2
a=5
print(a!=5)#= 装值，== 问是否相等，!= 问是否不等

#3
nianling=17
if nianling>60 or nianling<18:
    print("不通过")
elif nianling<=60:
    print("危险：着重观察")
elif nianling>=35:
    print("通过")
elif nianling>=25:
    print("优秀")
else:
    print("放行")

#4-5-6
score=-1
if score>100 and score<0:
    print("报错提示：输入有误请重新输入")
elif score>=90:
    print("优秀")
elif score>=80:
    print("良好")
elif score>=60:
    print("及格")
else :
    print("不及格")
#7
#print(我叫被当变量)
#print("我叫被当变量")
#8
age=26
shengao=1.82
name="张同学"
next_age=age+1
xuesheng=True
#if xuesheng:
    #texe="是"
#else:
    #texe="不是"
texe="是" if xuesheng else "不是"
print(f"我叫{name},身高{shengao}，明年{next_age}岁，我{texe}学生")