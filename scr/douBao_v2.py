import kimi
import json
from openai import OpenAI
with open('../config.json', encoding="utf-8") as f:
  cof = json.load(f)

client = OpenAI(
    api_key = cof["doubao"]["api-key"],
    base_url = "https://ark.cn-beijing.volces.com/api/v3",
)
history = []
for i in cof["system"]:
    history.append({"role":"system","content":i})

class chat(kimi.chat):
    def __init__(self,temperature=0.3,top_p=0.9,presence_penalty=0.5,max_tokens=1000):
        # 判断temperature是否在范围内
        self.temperature = 0.99 if temperature < 0 or temperature >= 2 else temperature
        # 判断top_p是否在范围内
        self.top_p = 1 if top_p < 0 or top_p >= 1 else top_p
        # 判断presence_penalty是否在范围内
        self.presence_penalty = (-2 if presence_penalty < -2 else (2 if presence_penalty > 2 else presence_penalty))
        self.max_tokens = max_tokens
        self.history = []
        for i in cof["system"]:
            self.history.append({"role": "system", "content": i})
        for i in cof["user_setting"]:
            self.history.append({"role": "system", "content": i})