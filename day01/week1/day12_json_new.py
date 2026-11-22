import json


# 保存账目：序列化，Python列表字典 → 写入json文件
def save_records(record_list):
    with open("account.json", "w", encoding="utf-8") as f:
        # ensure_ascii=False 中文正常显示，indent缩进美化
        json.dump(record_list, f, ensure_ascii=False, indent=2)

# 加载账目：反序列化，json文件 → 变回Python列表字典
def add_record(record_list, r_type, money, remark):#新增账目
    new_item={"r_type":r_type,
              "money":money,
              "remark":remark
              }
    record_list.append(new_item)
def show_all(record_list):#查看全部账目
    print("=====全部账目=====")
    for idx,item in  enumerate(record_list):
        print(f"{idx+1},类型：{item['r_type']}，金额：{item['money']}，备注：{item['remark']}")
def calc_balance(recordf_list):
    total_zongshouru = 0
    total_zongzhichu = 0
    for item in recordf_list:
        if item["r_type"]=="收入":
            total_zongshouru = total_zongshouru + item["money"]
        elif item["r_type"]=="支出":
            total_zongzhichu = total_zongzhichu + item["money"]
    balance = total_zongshouru - total_zongzhichu    
    return total_zongshouru,total_zongzhichu,balance
def load_records():
    try:
        with open("account.json", "r", encoding="utf-8") as f:
            data= json.load(f)
    except FileNotFoundError:
        print("文件不存在，返回空账本")
        data = []
    except json.JSONDecodeError:
        print("json文件损坏、格式乱了，兜底返回空列表，程序不崩溃")
        data = []
    except ValueError:
        print("数值转换失败")
        data = []
    return data
def delete_record(recordf_list):
    show_all(record_list)
    if len(record_list)==0:
        print("❌ 暂无账目，无法删除！")
    try:
        num=int(input("请输入要删除账目的序号："))
        idex=num-1
        if 0<= idex< len(record_list):
            confirm = input("确定要删除这条记录吗？(y/n):")
            if confirm == "y":
                del record_list[idex]
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
def xiugai_records(recordf_list):
    show_all(record_list)
    if len(record_list)==0:
        print("❌ 暂无账目，无法修改！")
        return
    try:
        num=int(input("请输入要修改账目的序号："))
        xiugai=num-1
        if 0<= xiugai< len(record_list):
            old_item = record_list[xiugai]
            print(f"旧数据：类型:{old_item['r_type']},金额:{old_item['money']},备注:{old_item['remark']}")
            new_rtype = input("请输入新的收支类型(收入/支出)：")
            if new_rtype not in ["收入","支出"]:
                print("❌ 收支类型错误！")
                return
            money_try = input("请输入新金额：")
            new_money = float(money_try)
            new_remark = input("请输入新备注：")
            if new_remark.strip() == "":
                print("❌ 备注不能为空！")
                return
            confir= input("确定要修改这条记录吗？(y/n):")
            if confir == "y":
                old_item["r_type"] = new_rtype
                old_item["money"] = new_money
                old_item["remark"] = new_remark
                save_records(record_list)
                print("✅ 修改成功！")
            else:
                print("❌ 已取消修改")
        else:
            print("❌ 序号不存在！")
    except ValueError:
        print("❌ 请输入合法数字！")
while True:
    print("\n=====个人账本=====")
    print("1.新增收支")
    print("2.查看全部账目")
    print("3.计算余额")
    print("4.删除错账")
    print("5.修改错账")
    print("0.退出")
    choice=input("请输入选择：")
    if choice=="1":
        while True:
            r_type=input("请输入（收入/支出）：".strip())
            if r_type=="收入"or r_type=="支出":
                break
            print("❌ 收支类型只能输入收入或者支出，请重新输入！")
        while True:
                money_try=(input("请输入金额："))
                try:
                    money = float(money_try)
                    if money <= 0:
                        print("❌ 金额必须大于0,请重新输入!")
                        continue
                    break
                except ValueError:
                        print("❌ 金额必须输入数字，添加失败！")
                        continue
        while True:
                remark=input("请输入备注：")
                if remark.strip() == "":
                    print("❌ 备注不能为空,请重新输入！")
                    continue
                break
        add_record(record_list, r_type, money, remark)
        save_records(record_list)# 新增完成，自动保存
        print("✅ 添加成功！")
    elif choice == "2":
        show_all(record_list)
    elif choice == "3":
        zongshouru, zongzhichu, bal = calc_balance(record_list)
        print(f"总收入：{zongshouru:.2f}，总支出：{zongzhichu:.2f}，余额：{bal:.2f}")
    elif choice == "4":
        delete_record(record_list)
    elif choice == "5":
        xiugai_records(record_list)
    elif choice == "0":
        print("程序退出")
        break
    else:
        print("❌ 输入错误，请重新选择！")
    # 保存
    # 读取
# 测试代码
# if __name__ == "__main__":
#     # 初始账目列表
#     records = [
#         {"r_type": "收入", "money": 3000, "remark": "工资"},
#         {"r_type": "支出", "money": 25, "remark": "奶茶,三分糖"}
#     ]
#     # 保存
#     save_records(records)
#     # 读取
#     res = load_records()
#     print(res)
#     print(type(res))
