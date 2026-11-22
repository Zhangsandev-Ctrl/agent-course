：return 写进循环内，函数提前退出，只拿到第一条数据。
改好之后运行看看结果。
def calc_avg(stu_list):
    zf=0
    for stu in stu_list:
        zf=zf + stu["score"]
        avg= zf/len(stu_list)
        return zf,avg#错误的
    return zf,avg#正确的

    变量缩进在函数外部，函数内无法访问。