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
# # 写入测试
# with open("test.txt", "w", encoding="utf-8") as f:
#     f.write("这是第一条测试内容")

# # 读取测试
# with open("test.txt", "w", encoding="utf-8") as f:
#     content = f.read()
# print(content)

# add_record(record_list,"收入",3000,"工资")
# print(record_list)
# add_record(record_list,"支出",150,"晚饭")
# show_all(record_list)
# income, out, bal = calc_balance(record_list)
# print(f"总收入：{income}，总支出：{out}，余额：{bal}")
def add_record(record_list, r_type, money, remark):#字典 `{"type":"收入/支出","money":金额,"remark":"备注"}`
    new_record={"type":r_type,
                "money":money,
                "remark":remark
                }
    record_list.append(new_record)
def show_all(record_list):
    print("=====全部账目=====")
    for idx, item  in enumerate(record_list):
        print(f"{idx+1},类型：{item['type']}，金额：{item['money']}，备注：{item['remark']}")
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
def save_records(record_list):
    with open("account.txt","w",encoding="utf-8")as f:#- `"w"`：覆盖写入；"a"`：追加写入；"r"`：读取文件。
        for item in (record_list):
            line = f'{item["type"]},{item["money"]},{item["remark"]}\n'
            f.write(line)
def load_records ():
    record_list=[]
    try :
        with open("account.txt", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                # parts[0] 收支类型，parts[1]金额，parts[2]备注
                item = {
                    "type":parts[0],
                    "money":float(parts[1]),
                    "remark":parts[2]
                }
                record_list.append(item)
    except FileNotFoundError:
        pass
    return record_list  
def  delete_record(record_list):
    show_all(record_list)
    if len(record_list)==0:
        print("❌ 暂无账目，无法删除！")
        return
    try:
        num=int(input("请输入要删除账目的序号："))
        index=num-1# 用户看到的序号是1开始，列表下标是0开始，所以减1
        if 0<= index<len(record_list):
            confirm = input("确定要删除这条记录吗？(y/n):")
            if confirm=="y":
                del record_list[index]
                save_records(record_list)
                print("✅ 删除成功！")
                save_records(record_list)
            else:
                print("❌ 已取消删除")
        else:
            print("❌ 序号不存在！")
    except ValueError:
        print("❌ 请输入合法数字！")
record_list = load_records()
while True:
    print("\n=====个人账本=====")
    print("1.新增收支")
    print("2.查看全部账目")
    print("3.计算余额")
    print("4.删除错账")
    print("0.退出")
    choice=input("请输入选择：")
    if choice=="1":
        r_type=input("请输入（收入/支出）：")
        money_try=(input("请输入金额："))
        try:
            money = float(money_try)
            remark=input("请输入备注：")
            if remark.strip() == "":
                print("❌ 备注不能为空！")
            else:
                add_record(record_list, r_type, money, remark)
                save_records(record_list)# 新增完成，自动保存
                print("✅ 添加成功！")
        except:
            print("❌ 金额必须输入数字，添加失败！")
    elif choice == "2":
        show_all(record_list)
    elif choice == "3":
        income, out, bal = calc_balance(record_list)
        print(f"总收入：{income:.2f}，总支出：{out:.2f}，余额：{bal:.2f}")
    elif choice == "4":
        delete_record(record_list)
    elif choice == "0":
        print("程序退出")
        break
    else:
        print("❌ 输入错误，请重新选择！")

