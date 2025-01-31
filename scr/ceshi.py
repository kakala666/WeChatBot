import requests
import json
import re
from datetime import date

# 直接获取今天的日期，返回一个date对象
today = date.today()
year = today.year
month = today.month
day = today.day
while True:
    date = input("请输入日期")
    match = re.match(r'^\d{4}-\d{2}-\d{2}$', date)
    if match:
        if (day + 14 < int(date[-2:]) or day - 1 > int(date[-2:] or int(date[5:7]) != int(month) or int(date[0:4] != year))):
            print("日期太过久远或太过超前")
            continue
        break
    else:
        print("日期输入有误，请重试")
        continue

url = "https://api.oioweb.cn/api/weather/weather?city_name=石家庄市"
re = requests.get(url=url).json()
print("aaa")
if(re["msg"] == "success"):
    city = re["result"]["city_name"]
    weather = re["result"]["current_condition"]
    weatherList = re["result"]["forecast_list"]
    tips = re["result"]["tips"]
    for i in weatherList:
        if i["date"] == date:
            weather=i["condition"]
            high_temperature = i["high_temperature"]
            low_temperature = i["low_temperature"]
            print(f"{city}{date}天气是{weather}\n最高气温{high_temperature}摄氏度,最低气温{low_temperature}摄氏度\n温馨提示{tips}")

    #print(f"今日{city}的天气是{weather}")
else:
    print("查询失败")