#需求：
#1. 使用列表嵌套字典存储多名学生信息（姓名、分数）
#2. 封装函数 `get_level(score)` 返回等级
#3. 封装函数 `calc_avg(stu_list)`，返回总分、平均分
#4. 遍历学生列表，打印每个学生姓名、分数、对应等级
#5. 关键代码行添加注释
stu_list = [
    {"name":"小红", "score":91},
    {"name":"小明", "score":78},
    {"name":"小张", "score":66},
    {"name":"小孟", "score":59}]
def get_level(score):
    if score>=90:
        return "优秀"
    elif score >=70:
        return "良好"
    elif score >= 60:
        return "及格"
    else :
        return "不及格"
def calc_avg(stu_list):
    zf=0
    for stu in stu_list:
        zf=zf + stu["score"]
        avg= zf/len(stu_list)
    return zf,avg
for student in stu_list:
    name=student["name"]
    s=student["score"]
    level=get_level(s)
    print(f"姓名：{name},分数:{s},等级:{level}")
zf_score, avg_score = calc_avg(stu_list)
print(f"\n总分:{zf_score},平均分:{avg_score:.2f}")