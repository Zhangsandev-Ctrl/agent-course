# Day8 片段存档 · 函数 return 位置

> 用途：记录"return 写在循环内部会导致函数提前退出"这个坑，完整知识点见《Python基础_面试复习手册.md》。

## 错误写法

```python
def calc_avg(stu_list):
    zf = 0
    for stu in stu_list:
        zf = zf + stu["score"]
        avg = zf / len(stu_list)
        return zf, avg          # ❌ 第一次循环就 return，只算到第一条
```

## 正确写法

```python
def calc_avg(stu_list):
    zf = 0
    for stu in stu_list:
        zf = zf + stu["score"]
    avg = zf / len(stu_list)     # 累加完再算平均
    return zf, avg               # ✅ return 放在循环外面
```

## 本日考点

1. `return` 执行后函数立即结束，写在循环体内等于只处理第一条数据。
2. 需要汇总全部数据时，循环只负责累加，计算和 `return` 放在循环外。
3. 变量缩进在函数外部，函数内无法访问（作用域坑）。
4. 本日踩坑已同步收进 `error_book.md` D9–D10 条目。
