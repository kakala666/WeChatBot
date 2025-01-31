import requests

# 目标网页的 URL
url = 'http://example.com'
# 发送 GET 请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 网页内容在 response.text 中
    html_content = response.text
    print(html_content)
else:
    print('请求失败，状态码：', response.status_code)