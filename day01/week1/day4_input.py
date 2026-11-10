#要求：

#1. input 接收身高、体重，float 转换
#2. f-string 输出，BMI 保留 2 位小数
#3. 代码加中文注释
sg=input("身高：")#接收用户输入的身高
tz=input('体重：')#接收用户输入的体重
sg=float(sg)#转换类型
tz=float(tz)#转换类型
if sg<=0 or tz<=0:
    print("输入错误请重新收入")
else:
    BMI=tz / sg ** 2
    print(f'大家好，我叫z，我的身高{sg}米，我的体重{tz:.2f}kg，我的BMI:{BMI:.2f}')#f-string 输出
    #跑通之后，我们再加判断：BMI 偏瘦 / 正常 / 超重
    if BMI>=30:
        print("超重")
    elif BMI>=20:
        print("正常")
    else :
     print("偏瘦")