name_list = ["张三","李四","王五","赵六","张小花","李磊"]
score_list = [92, 55, 78, 83, 67, 89]
#1. 统计**及格（≥60）**一共有多少人
#2. 同时打印出所有及格同学的名字和分数
#3. 最后单独输出一句：及格总人数：XX
count = 0
for i in range(len(name_list)):
    name=name_list[i]
    score=score_list[i]
    if score>=60:
        count=count+1
        jg='及格'
        print(f'{name},{score}分，评级：{jg}')
print('总人数：',count)