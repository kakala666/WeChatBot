import os
from typing import Union

from openai import OpenAI
import json
with open('../config.json', encoding="utf-8") as f:
  cof = json.load(f)
client = OpenAI(
    api_key="sk-01cb5ab86ebd4b60b04909e1cdef475c",  # 如果您没有配置环境变量，请在此处用您的API Key进行替换
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # 填写DashScope服务的base_url
)
completion = client.chat.completions.create(
    model="qwen-turbo",
    messages=[
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': '你是谁？'}],
    extra_body={
        "enable_search": True
    }
)
history = []



class chat():
    def __init__(self,temperature=0.3,top_p=0.9,presence_penalty=0.5,max_tokens=1000):
        print("构建通义千寻")
        # 判断temperature是否在范围内
        self.temperature = 0.99 if temperature < 0 or temperature >= 2 else temperature
        # 判断top_p是否在范围内
        self.top_p = 1 if top_p < 0 or top_p >= 1 else top_p
        # 判断presence_penalty是否在范围内
        self.presence_penalty = (-2 if presence_penalty < -2 else (2 if presence_penalty > 2 else presence_penalty))
        self.max_tokens = max_tokens
        self.history = []
        for i in cof["system"]:
            if not i is None:
                self.history.append({"role": "system", "content": i})
        for i in cof["user_setting"]:
            if not i is None:
                self.history.append({"role": "system", "content": i})
    def Inheritance(self,history):
        self.history = history
    def get_history(self):
        return self.history
    def set_bot(self, bot_type, value:Union[float,int]):
        setattr(self, bot_type, value)
    def chat(self,query):
        self.history.append({
            "role": "user",
            "content": query
        })
        completion = client.chat.completions.create(
            model="qwen-turbo",
            messages=self.history,
            temperature=self.temperature,  # 采样温度，用于控制模型生成文本的多样性。temperature越高，生成的文本更多样，反之，生成的文本更确定。取值范围： [0, 2)
            top_p=self.top_p,  # 核采样的概率阈值，用于控制模型生成文本的多样性。top_p越高，生成的文本更多样。反之，生成的文本更确定。取值范围： [0, 1]
            # 控制模型生成文本时的内容重复度。
            # 取值范围：[-2.0, 2.0]。正数会减少重复度，负数会增加重复度。
            # 适用场景：
            # 较高的presence_penalty适用于要求多样性、趣味性或创造性的场景，如创意写作或头脑风暴。
            # 较低的presence_penalty适用于要求一致性或专业术语的场景，如技术文档或其他正式文档。
            presence_penalty=self.presence_penalty,
            max_tokens=self.max_tokens,  # 生成文本的最大长度。取值范围
        )
        result = completion.choices[0].message.content
        self.history.append({
            "role": "assistant",
            "content": result
        })
        return result