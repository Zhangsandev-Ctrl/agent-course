# import json
# def save_records(record_list):
#     with open("account.json", "w", encoding="utf-8") as f:
#         # ensure_ascii=False 中文正常显示，indent缩进美化
#         json.dump(record_list, f, ensure_ascii=False, indent=2)
# def load_records():
#     record_list = []
#     dirty_count = 0
#     try:
#         with open("account.json", "r", encoding="utf-8") as f:
#             raw_list = json.load(f)
#     except FileNotFoundError:
#         return [], 0
#     except json.JSONDecodeError:
#         return [], 1
#     # 遍历每一条，校验
#     for item in raw_list:
#         # 校验规则：必须包含这3个key
#         if not isinstance(item, dict):
#             dirty_count += 1
#             continue
#         if "r_type" not in item or "money" not in item or "remark" not in item:
#             dirty_count += 1
#             continue
#         # 校验金额必须是数字
#         if not isinstance(item["money"], (int, float)):
#             dirty_count += 1
#             continue
#         # 全部校验通过，加入正常列表
#         record_list.append(item)
#     return record_list, dirty_count
import json
import os

def save_records(record_list):
    with open("account.json", "w", encoding="utf-8") as f:
        json.dump(record_list, f, ensure_ascii=False, indent=2)

def load_records():
    record_list = []
    dirty_count = 0
    try:
        with open("account.json", "r", encoding="utf-8") as f:
            raw_list = json.load(f)
    except FileNotFoundError:
        # 文件压根不存在，新建空账本
        return [], 0
    except json.JSONDecodeError:
        # 文件存在，但是JSON语法坏掉：先备份
        backup_name = "account_broken.json.bak"
        os.rename("account.json", backup_name)
        print(f"⚠️ JSON文件损坏，已备份为 {backup_name}，将使用空账本启动")
        return [], 0

    # 走到这里：JSON语法没问题，逐条校验每一条账目
    for item in raw_list:
        # 校验1：必须是字典
        if not isinstance(item, dict):
            dirty_count += 1
            continue
        # 校验2：必须包含三个必填key
        if "r_type" not in item or "money" not in item or "remark" not in item:
            dirty_count += 1
            continue
        # 校验3：money必须是数字（int/float）
        if not isinstance(item["money"], (int, float)):
            dirty_count += 1
            continue
        return record_list, dirty_count

