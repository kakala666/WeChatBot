import os
from openai import OpenAI
import json
from pathlib import Path
from typing import Union



class chat():
    def __init__(self,temperature=0.3,top_p=0.9,presence_penalty=0.5,max_tokens=1000):
        with open('../config.json', encoding="utf-8") as f:
            self.cof = json.load(f)
        self.client = OpenAI(
            api_key=self.cof["doubao"]["api-key"],
            base_url="https://ark.cn-beijing.volces.com/api/v3",
        )

        #判断temperature是否在范围内
        self.temperature = 0.99 if temperature < 0 or temperature >= 2 else temperature
        #判断top_p是否在范围内
        self.top_p = 1 if top_p < 0 or top_p >= 1 else top_p
        #判断presence_penalty是否在范围内
        self.presence_penalty = (-2 if presence_penalty < -2 else (2 if presence_penalty > 2 else presence_penalty))
        self.max_tokens = max_tokens
        self.history = []
        for i in self.cof["system"]:
            self.history.append({"role": "system", "content": i})
        for i in self.cof["user_setting"]:
            self.history.append({"role": "system", "content": i})

    def init_file(self,filepath:str):
        file_object = self.client.files.create(file=Path(filepath), purpose="file-extract")
        file_content = self.client.files.content(file_id=file_object.id).text
        return file_content
    def set_bot(self,type,value:Union[float,int]):
        if type == "temperature":
            self.temperature = value
            print(f'temperature调整为{self.temperature}')
            return f'temperature调整为{self.temperature}'
        elif type == "top_p":
            self.top_p = value
            print(f'top_p调整为{self.top_p}')
            return f'top_p调整为{self.top_p}'
        elif type == "presence_penalty":
            self.presence_penalty = value
            print(f'presence_penalty调整为{self.presence_penalty}')
            return f'presence_penalty调整为{self.presence_penalty}'
        elif type == "max_tokens":
            self.max_tokens = value
            print(f'max_tokens调整为{self.max_tokens}')
            return f'max_tokens调整为{self.max_tokens}'
    def Inheritance(self,history):
        self.history = history
    def get_history(self):
        return self.history
    def chat(self,query):
        self.history.append({
            "role": "user",
            "content": query
        })
        completion = self.client.chat.completions.create(
            model=self.cof["doubao"]["bot-id"],
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
"""while True:
    query = input("请输入问题：")
    if query == "exit":
        break
    print(chat().chat(query))"""