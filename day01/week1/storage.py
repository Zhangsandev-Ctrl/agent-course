import json
import os

# 基于本脚本所在目录逐级向上定位项目根目录，不依赖运行时的当前工作目录
def _find_account_file():
    cur = os.path.dirname(os.path.abspath(__file__))
    while True:
        candidate = os.path.join(cur, "account.json")
        if os.path.exists(candidate):
            return candidate
        parent = os.path.dirname(cur)
        if parent == cur:  # 已到磁盘根目录，仍未找到
            return os.path.join(cur, "account.json")
        cur = parent

ACCOUNT_FILE = _find_account_file()


def save_records(record_list):
    with open(ACCOUNT_FILE, "w", encoding="utf-8") as f:
        json.dump(record_list, f, ensure_ascii=False, indent=2)


def load_records():
    record_list = []
    dirty_count = 0
    try:
        with open(ACCOUNT_FILE, "r", encoding="utf-8") as f:
            raw_list = json.load(f)
    except FileNotFoundError:
        # 文件压根不存在，新建空账本
        return [], 0
    except json.JSONDecodeError:
        # 文件存在，但 JSON 语法损坏：先备份，再按空账本启动
        backup_name = os.path.join(os.path.dirname(ACCOUNT_FILE), "account_broken.json.bak")
        os.rename(ACCOUNT_FILE, backup_name)
        print(f"⚠️ JSON文件损坏，已备份为 {os.path.basename(backup_name)}，将使用空账本启动")
        return [], 0

    # JSON 语法没问题，逐条校验每一条账目
    for item in raw_list:
        # 校验1：必须是字典
        if not isinstance(item, dict):
            dirty_count += 1
            continue
        # 校验2：必须包含三个必填 key
        if "r_type" not in item or "money" not in item or "remark" not in item:
            dirty_count += 1
            continue
        # 校验3：money 必须是数字（排除 bool）
        if isinstance(item["money"], bool) or not isinstance(item["money"], (int, float)):
            dirty_count += 1
            continue
        # 全部校验通过，才加入干净列表
        record_list.append(item)

    # 循环全部遍历完，再统一返回，不能写在循环里面
    return record_list, dirty_count
