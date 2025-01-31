import os
from volcenginesdkarkruntime import Ark

client = Ark(api_key=os.environ.get("ARK_API_KEY"))

print("----- multiple rounds request -----")
completion = client.chat.completions.create(
    model="<YOUR_ENDPOINT_ID>",
    messages = [
        {"role": "system", "content": "你是豆包，是由字节跳动开发的 AI 人工智能助手"},
        {"role": "user", "content": "花椰菜是什么？"},
        {"role": "assistant", "content": "花椰菜又称菜花、花菜，是一种常见的蔬菜。"},
        {"role": "user", "content": "再详细点"},
    ],
)
print(completion.choices[0].message.content)