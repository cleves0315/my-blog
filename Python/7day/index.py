import requests

# url = 'https://baidu.com'
url = 'https://api.github.com/users/cleves0315'
# url = 'https://mp.weixin.qq.com/s/J68hA0ncRR_q91ccVINP0g' # 公众号文章
headers = {}
data = {}

response = requests.get(url, json=data, headers=headers)

# 获取响应状态码
print('状态码：', response.status_code)
print('\n')
# 获取响应头
print('响应头信息：', response.headers)
print('\n')
# 获取响应正文
print('响应正文：', response.text)
print('\n')
