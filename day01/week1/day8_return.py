def say_hi():# 定义
    print('你好')# 调用
#**参数（形参、实参）**：给函数传数据，让函数更灵活
def say_hi1(name):
    print(f"你好，{name}")
say_hi1('张三')
#**return 返回值**：把计算结果给到外面，函数遇到 return 就停止执行
#重点区分：`print`只是打印给人看；`return`是把结果交给代码继续用
def add(a,b):
    res = a + b
    return res
result=add(3,5)
print(result)
#多个参数、return 可以返回多个值
def get_level(score):
    if score >=90:
        return'优秀'
    elif score >=80:
        return'良好'
    elif score >=60:
        return'及格'
    else:
        return'不及格'
print(get_level(92))
print(get_level(80))
print(get_level(71))
print(get_level(61))
print(get_level(59))
#列表嵌套字典结构示例
stu_list = [
    {"name":"小红", "score":90},
    {"name":"小明", "score":78}
]
#基础函数定义、带参数、return 返回
def get_level(score):
    if score >= 90:
        return "优秀"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"
