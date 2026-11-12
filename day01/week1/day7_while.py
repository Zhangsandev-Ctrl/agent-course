#while 条件:#循环内代码
num=1
while num<=5:
    print(num)
    num=num+1# 一定要写！不然条件永远成立，死循环
num=1
while num <=10:
    if num == 6:
        break#break（直接跳出 while 循环）
    print(num)
    num=num+1
num=0
while num <=5:
    num=num+1
    if num == 3:
        continue#continue（跳过本次，直接下一轮）
    print(num)

