from storage import load_records, save_records
from ledger import add_record, show_all, calc_balance, delete_record, xiugai_records
def main():
    record_list,dirty_count = load_records()
    if dirty_count > 0:
        save_records(record_list)
        print(f"✅ 检测到 {dirty_count} 条脏账目，已经自动清理")
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
                r_type=input("请输入（收入/支出）：").strip()
                if r_type=="收入"or r_type=="支出":
                    break
                print("❌ 收支类型只能输入【收入】或者【支出】，请重新输入！")
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
                    remark=input("请输入备注：").strip()
                    if remark.strip() != "":
                        break
                    print("❌ 备注不能为空,请重新输入！")
                    
            changed = add_record(record_list, r_type, money, remark)
            if changed:
                print("✅ 添加成功！")
                save_records(record_list)
        elif choice == "2":
            show_all(record_list)
        elif choice == "3":
            zongshouru, zongzhichu, bal = calc_balance(record_list)
            print(f"总收入：{zongshouru:.2f}，总支出：{zongzhichu:.2f}，余额：{bal:.2f}")
        elif choice == "4":
            changed = delete_record(record_list)
            if changed:
                save_records(record_list)
            #delete_record(record_list)
        elif choice == "5":
            changed = xiugai_records(record_list)
            if changed:
                save_records(record_list)
            #xiugai_records(record_list)
        elif choice == "0":
            print("程序退出")
            break
        else:
            print("❌ 输入错误，请重新选择！")

if __name__ == "__main__":
    main()
# - **storage.py**：只负责 JSON 读写；
# - **ledger.py**：只操作列表，return 布尔值，不直接保存文件；
# - **main.py**：交互入口，依据返回值决定是否持久化。