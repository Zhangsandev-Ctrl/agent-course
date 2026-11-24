while True:
    try:
        xs = input("请输入被除数（输 q 退出）：")
        if xs == "q":
            break
        ys = input("请输入除数：")
        x = int(xs)
        y = int(ys)
        result = x / y
    except ZeroDivisionError as e:
        print("出错了：除数不能为 0")
        print("错误信息：", e)
    except ValueError as e:
        print("出错了：数值不合法")
        print("错误信息：", e)
    else:
        print("计算成功，结果：",result)
    finally:
        print("本轮结束")
