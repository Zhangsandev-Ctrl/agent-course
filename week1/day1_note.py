from openai import OpenAI # 导入 openai 库里的 OpenAI 工具，用来和大模型服务对话
# 连接本地ollama服务
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="dummy"  # 本地ollama不需要真实key，随便填一个占位
)
# 创建连接客户端，指定本地 ollama 服务地址，本地模型不用真实密钥
response = client.chat.completions.create(
    model="deepseek-r1:1.5b",
    messages=[
        {"role": "user", "content": "用一句话介绍什么是Agent智能体"}
    ]
)
# 向模型发送对话请求，指定模型、用户提问内容
print(response.choices[0].message.content)
# 提取模型返回的回答文本，打印输出到终端# print() 把括号里的内容输出到终端