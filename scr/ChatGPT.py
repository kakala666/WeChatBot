import requests
import kimi
import json
from typing import Union
from pathlib import Path

class Chat(kimi.chat):
  def __init__(self,temperature=0.3,top_p=0.9,presence_penalty=0.5,max_tokens=1000):
    with open('../config.json', encoding="utf-8") as f:
      cof = json.load(f)
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

    self.headers = {
      'Accept': 'application/json',
      'Authorization': 'Bearer sk-5to1i3DWqwoJREzV2GLa7daLdOTJpN33THfR5oN9mjkkMZu2',
      'Content-Type': 'application/json'
    }
    self.data = {
      "model": "gpt-4o",
      "messages": [
        {
          "role": "system",
          "content": "你是我的人工智能助手"
        },
        {
          "role": "user",
          "content": "你好"
        }
      ]
    }
    self.url = 'https://api.wlai.vip/v1/chat/completions'
  def setBot(self,setting,value):
    if setting == 'temperature':
      value = int(value)
      if value>=0 and value<=2:
        self.temperature = value
    elif setting == 'top_p':
      pass
  def chat(self, query):
    self.history.append({
      "role": "user",
      "content": query
    })
    msg = {
      "model": "gpt-4o",
      "temperature":self.temperature,
      "top_p":self.top_p,
      "presence_penalty":self.presence_penalty,
      "max_tokens":self.max_tokens,
      "messages": self.history
    }
    result = requests.post(url=self.url,headers=self.headers,json=msg).json().get('choices')[0].get('message').get('content')
    self.history.append({
      "role": "assistant",
      "content": result
    })
    return result








