# 1. 用列表存放多条收支字典
# 2. 封装函数 `add_record(record_list, r_type, money, remark)`：追加记录
# 3. 封装函数 `calc_balance(record_list)`：return 总收入、总支出、余额
# 4. 封装函数 `show_all(record_list)`：循环打印每一条记录
# 5. while 主循环菜单：
#    - 1：新增收支
#    - 2：查看全部账目
#    - 3：计算余额
#    - 0：退出
# 6. 输入校验：
#    - 输入备注时用`strip()`，空内容不让保存
#    - 金额必须是数字，非法输入提示，不直接报错崩溃
# 7. 关键代码行写注释
def add_record(record_list, r_type, money, remark):#字典 `{"type":"收入/支出","money":金额,"remark":"备注"}`
    new_record={"type":r_type,
                "money":money,
                "remark":remark
                }
    record_list.append(new_record)
def show_all(record_list):
    print("=====全部账目=====")
    for item  in record_list:
        print(f"类型：{item['type']}，金额：{item['money']}，备注：{item['remark']}")
def calc_balance(record_list):
    total_income = 0
    total_out = 0
    for item in record_list:
        if item ["type"]=="收入":
             total_income =  total_income + item['money']
        elif item ["type"]=="支出":
            total_out = total_out + item['money']
    balance = total_income - total_out
    return total_income, total_out, balance
record_list = []
while True:
    print("\n=====个人账本=====")
    print("1.新增收支")
    print("2.查看全部账目")
    print("3.计算余额")
    print("0.退出")
    choice=input("请输入选择：")
    if choice=="1":
        r_type=input("请输入（收入/支出）：")
        money_try=(input("请输入金额："))
        try:
            money = float(money_try)
            remark=input("请输入备注：")
            add_record(record_list, r_type, money, remark)
            print("✅ 添加成功！")
        except:
            print("❌ 金额必须输入数字，添加失败！")
    elif choice == "2":
        show_all(record_list)
    elif choice == "3":
        income, out, bal = calc_balance(record_list)
        print(f"总收入：{income:.2f}，总支出：{out:.2f}，余额：{bal:.2f}")
    elif choice == "0":
        print("程序退出")
        break
    else:
        print("❌ 输入错误，请重新选择！")
# add_record(record_list,"收入",3000,"工资")
# print(record_list)
# add_record(record_list,"支出",150,"晚饭")
# show_all(record_list)
# income, out, bal = calc_balance(record_list)
# print(f"总收入：{income}，总支出：{out}，余额：{bal}")