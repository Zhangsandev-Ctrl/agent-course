1. `for score in score_list`：逐个取出列表里的元素
2. `total = total + score`：累加求和
3. `len(score_list)`：统计列表里面元素个数
4. **打擂台思路**：先拿第一个值当标杆，循环逐个对比，遇到更大 / 更小就替换标杆（不使用 max ()、min ()，是面试常考写法）

score_list = [85, 92, 76, 59, 98]
total = 0
# 打擂台初始值：先拿第一个分数当临时最高分、最低分
max_score = score_list[0]
min_score = score_list[0]

for score in score_list:
    print("成绩：", score)
    total = total + score
    # 擂台：如果当前分数比临时最高分更大，就更新最高分
    if score > max_score:
        max_score = score
    # 擂台：如果当前分数比临时最低分更小，就更新最低分
    if score < min_score:
        min_score = score

avg = total / len(score_list)
print("总分：", total)
print("平均分：", avg)
print("最高分：", max_score)
print("最低分：", min_score)
（print 少逗号、range 不能直接放列表）写到 `notes/day5.md`
