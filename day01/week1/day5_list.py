#1. **列表定义** `[]`：有序、可改、能放多个数据
#score_list = [85, 92, 76, 59, 98]
#2. **索引**：从 0 开始；`[0]` 取第一个，`[-1]` 取最后一个
#3. **增删改**：`append()` 追加、`列表[下标]=新值` 改、`pop()/remove()` 删
#4. **for 遍历**：`for s in score_list:` 缩进里的代码对每个元素跑一遍
#5. `range()` 先混个脸熟（明天 D6 细讲）

## 独立作业 `week1/day5_list.py`

#1. 列表：`[85, 92, 76, 59, 98]`
#2. for 循环打印每一个成绩
#3. 算出**总分、平均分**
#4. 找出**最高分、最低分**（用遍历 + 打擂台方式，不用 max/min）
#5. 关键行写中文注释
score_list = [85, 92, 76, 59, 98]#列表：`[85, 92, 76, 59, 98]`
total=0# 总和盒子，初始是空的，先设为0
for score in score_list:
    print("成绩：",score)#for 循环打印每一个成绩
    total=total+score#算出**总分*
print("总分：",total)#打印出**总分**
avg=total/len(score_list)#算出**平均分**len长度个数
print("平均分：",avg)#打印出**平均分**
max_score=score_list[0]#先设 `max_score = score_list[0]`
min_score=score_list[0]#先设 `min_score = score_list[0]`
for score in score_list:#遍历列表
    if score>max_score:#遍历里判断遇到更大的就替换
        max_score=score
    if score<min_score:#遍历里判断遇到更小的就替换
        min_score=score
print("最高分：",max_score)#输出打印最高分
print("最低分：",min_score)#输出打印最低分

#练习 1
#需求：
#列表 `[12, 5, 33, 19, 26]`
#1. 循环打印每一个数字
#2. 计算总和、平均值
#3. 找出最大值、最小值
lianxi_list=[12, 5, 33, 19, 26]
he=0
for lianxi in lianxi_list:
    print('练习：',lianxi)
    he=he+lianxi
print('总和：',he)
pjz=he/len(lianxi_list)
print('平均值：',pjz)
max_lianxi=lianxi_list[0]
min_lianxi=lianxi_list[0]
for lianxi in lianxi_list:
    if lianxi>max_lianxi:
        max_lianxi=lianxi
    if lianxi < min_lianxi:
        min_lianxi=lianxi
print('最大值：',max_lianxi)
print('最小值：',min_lianxi)

#练习 2
#需求：
#列表 `["苹果","香蕉","橙子","葡萄"]`
#1. for 循环逐个打印水果名字
#2. 算出一共有多少种水果（用 len）
sg_list=["苹果","香蕉","橙子","葡萄"]
#sg=str(sg)
for sg in sg_list:
    print(sg)
zs=len(sg_list)
print('多少种水果：',zs,'种')