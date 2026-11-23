# Day5 片段存档 · 列表遍历与打擂台

> 用途：面试常考的"不用 max() 求最值"写法，完整知识点见《Python基础_面试复习手册.md》。

```python
score_list = [85, 92, 76, 59, 98]
total = 0
# 打擂台初始值：先拿第一个分数当临时最高分、最低分
max_score = score_list[0]
min_score = score_list[0]

for score in score_list:
    print("成绩：", score)
    total = total + score
    # 擂台：当前分数比临时最高分更大，就更新最高分
    if score > max_score:
        max_score = score
    # 擂台：当前分数比临时最低分更小，就更新最低分
    if score < min_score:
        min_score = score

avg = total / len(score_list)
print("总分：", total)
print("平均分：", avg)
print("最高分：", max_score)
print("最低分：", min_score)
```

## 本日考点

1. `for score in score_list`：逐个取出列表元素，不需要下标时用这种写法。
2. `total = total + score`：累加求和。
3. `len(score_list)`：元素个数，用于求平均。
4. **打擂台思路**：先拿第一个值当标杆，循环逐个比较，更大 / 更小就替换标杆；不依赖 `max()` / `min()`，面试常考手写。
5. 本日踩坑（已入 error_book）：`print` 少逗号、`range` 里不能直接放列表。
