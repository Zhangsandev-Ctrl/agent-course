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

def delete_record(record_list):
    show_all(record_list)
    if len(record_list)==0:
        print("❌ 暂无账目，无法删除！")
        return False
    try:
        num=int(input("请输入要删除账目的序号："))
        idex=num-1
        if 0<= idex< len(record_list):
            confirm = input("确定要删除这条记录吗？(y/n):")
            if confirm == "y":
                del record_list[idex]
                print("✅ 删除成功！")
                return True
            else:
                print("❌ 已取消删除")
                return False
        else:
            print("❌ 序号不存在！")
            return False
    except ValueError:
        print("❌ 请输入合法数字！")
        return False

def xiugai_records(record_list):
    show_all(record_list)
    if len(record_list) == 0:
        print("❌ 暂无账目，无法修改！")
        return False
    try:
        num = int(input("请输入要修改账目的序号："))
        idx = num - 1
        if 0 <= idx < len(record_list):
            old_item = record_list[idx]
            print(f"旧数据：类型:{old_item['r_type']},金额:{old_item['money']},备注:{old_item['remark']}")

            # 收支while校验
            while True:
                new_type = input("请输入新的收支类型(收入/支出):").strip()
                if new_type in ["收入", "支出"]:
                    break
                print("❌ 收支类型错误！只能输入【收入】或【支出】")
            
            # 金额while校验
            while True:
                try:
                    new_money = float(input("请输入新金额：").strip())
                    if new_money > 0:
                        break
                    print("❌ 金额必须大于0！")
                except ValueError:
                    print("❌ 金额必须是数字！")
            
            # 备注while校验
            while True:
                new_remark = input("请输入新备注：").strip()
                if new_remark != "":
                    break
                print("❌ 备注不能为空！")

            confirm = input("确定要修改这条记录吗？(y/n):")
            if confirm == "y":
                old_item["r_type"] = new_type
                old_item["money"] = new_money
                old_item["remark"] = new_remark
                print("✅ 修改成功！")
                return True  # 修改成功，告诉main需要保存
            else:
                print("❌ 已取消修改")
                return False
        else:
            print("❌ 序号不存在！")
            return False
    except ValueError:
        print("❌ 请输入合法数字！")
        return False