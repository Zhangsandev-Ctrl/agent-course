"""Day1 冒烟测试：验证你的 API Key 和网络是否跑通。

用法：
    1. 打开同目录上一级的 .env，填 PLATFORM 和对应 Key
    2. 在 D:\dev\agent-course 目录下运行：
       D:\dev\Python311\python.exe day01\hello_llm.py
"""
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

# 项目根目录（.env 就在这一级）
ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

# 三家平台都兼容 OpenAI 接口，只是地址和模型名不同
PLATFORMS = {
    "deepseek": {
        "base_url": "https://api.deepseek.com/v1",
        "model": "deepseek-chat",
        "key_name": "DEEPSEEK_API_KEY",
    },
    "bailian": {
        "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "model": "qwen-plus",
        "key_name": "DASHSCOPE_API_KEY",
    },
    "zhipu": {
        "base_url": "https://open.bigmodel.cn/api/paas/v4",
        "model": "glm-4-flash",
        "key_name": "ZHIPU_API_KEY",
    },
}


def main() -> int:
    platform = os.getenv("PLATFORM", "deepseek").strip().lower()
    cfg = PLATFORMS.get(platform)
    if cfg is None:
        print(f"[错误] .env 里的 PLATFORM={platform} 不认识，可选：deepseek / bailian / zhipu")
        return 1

    api_key = os.getenv(cfg["key_name"], "").strip()
    if not api_key:
        print(f"[提示] 你还没填 {cfg['key_name']}。")
        print(f"       打开 {ROOT / '.env'}，把 Key 粘到 {cfg['key_name']}= 后面，保存后重新运行。")
        return 1

    print(f"[信息] 平台={platform} 模型={cfg['model']}")
    client = OpenAI(api_key=api_key, base_url=cfg["base_url"])

    try:
        resp = client.chat.completions.create(
            model=cfg["model"],
            messages=[
                {"role": "system", "content": "你是一个简洁的助手，回答不超过两句话。"},
                {"role": "user", "content": "用一句大白话解释：什么是 API？"},
            ],
            temperature=0.3,
        )
    except Exception as exc:
        print(f"[调用失败] {type(exc).__name__}: {exc}")
        print("       常见原因：Key 填错、没实名/没额度、网络到不了该平台。")
        return 1

    print("\n模型回复：")
    print(resp.choices[0].message.content)
    print(f"\n[Token 用量] prompt={resp.usage.prompt_tokens} completion={resp.usage.completion_tokens}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
from openai import OpenAI

# 连接本地ollama服务
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="dummy"  # 本地ollama不需要真实key，随便填一个占位
)

response = client.chat.completions.create(
    model="deepseek-r1:1.5b",
    messages=[
        {"role": "user", "content": "用一句话介绍什么是Agent智能体"}
    ]
)

print(response.choices[0].message.content)
