#1. `range(结束数字)`：`range(5)` → 生成 0,1,2,3,4
#2. `range(起始,结束)`：`range(2,6)` → 2,3,4,5（**左闭右开，取不到结束值**）
#3. `range(起始,结束,步长)`：`range(1,10,2)` → 1,3,5,7,9，每次 + 2
#4. 搭配 for：`for `

## 独立作业 week1/day6_range.py

#1. 用 range 打印 1~10
#2. 用 range 求 1 到 100 的累加和
#3. 结合列表：`score_list = [88,72,90,66]`，用 `for i in range(len(score_list))` 方式，打印下标 + 对应分数
#> 提示：`score_list[i]` 取出下标 i 对应的元素

for i in range(5):
    print(i)

for z in range(2,7):
    print(z)
for n in range(1,10,1):
    print(n)

#1. 用 range 打印 1~10
for j in range(1,11):
    print(j)
#2. 用 range 求 1 到 100 的累加和
k=0
for h in range(1,101):
    k=k+h
print('总和：',k)
#结合列表：`score_list = [88,72,90,66]`，用 `for i in range(len(score_list))` 方式，打印下标 + 对应分数
score_list = [88,72,90,66]
for i in range(len(score_list)):
    print(score_list[i])

name_list = ["小明", "小红", "小刚", "小丽",'张三','张四']
score_list = [88,72,90,66,99,100]
#- 下标 1 → 名字小红，分数 72
#需求：输入名字，循环遍历，找到名字匹配的下标，再拿这个下标取出分数。
input_xing=input('请输入姓氏：')
has_find=False
for i in range(len(name_list)):
    name=name_list[i]# 取名字第一个字，对比输入的姓氏
    if name[0]==input_xing:
        print(f'{name}的分数是{score_list[i]}')
        has_find=True
if not has_find:
    print('查无此人，请重新输入！')
