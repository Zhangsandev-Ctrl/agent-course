
#score=95
#score=82
#score=60
#score=55
#score=105
score=3
if score>100 or score<0:
    print("报错:成绩不合法请重新输入")
elif score>=90:
    print("优秀")
elif score>=80 :
    print("良好")
elif score>=60:
    print("及格")
else: 
    print("不及格")

#在 `score_helper.py` 改造，要求：

#- 变量存：`name`、`score_chinese`、`score_math`、`score_english` 三科分数；
#- 计算打印：总分 total、平均分 avg；
#- 平均分评级：≥90 优秀 / ≥80 良好 / ≥60 及格 / 否则不及格；
#- 任一原始分数 <0 或者>100，先提示分数不合法；
#- 关键代码写中文注释
name="张同学"#名字
score_chinese=105#分数1
score_math=82#分数2
score_english=92#分数3
if score_chinese>100 or score_chinese<0 or score_english>100 or score_english<0 or score_math>100 or score_math<0:
    print("分数不合法")#任一原始分数 <0 或者>100，先提示分数不合法
else:
    total=score_chinese+score_english+score_math#总分
    avg=total/3#平均分
    print(f"我叫{name}，总分{total},平均分:{avg:.2f}")
    if avg>=90:
        print("优秀")
    elif avg>=80:
        print("良好")
    elif avg>=60:
        print("及格")
    else:
        print("不及格")#平均分评级：≥90 优秀 / ≥80 良好 / ≥60 及格 / 否则不及格