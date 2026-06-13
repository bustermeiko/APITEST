import requests

# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests

r = requests.get('https://api.github.com/events')
print(r.status_code)  # 状态码
print(r.text)  # 返回文本
print(r.json())  # 返回json数据


