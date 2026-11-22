import json
def save_records(record_list):
    with open("account.json", "w", encoding="utf-8") as f:
        # ensure_ascii=False 中文正常显示，indent缩进美化
        json.dump(record_list, f, ensure_ascii=False, indent=2)
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
