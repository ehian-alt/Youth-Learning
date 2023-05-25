import time
import requests
import json

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

# 每一期青年大学习的基本信息url
info_url = 'http://www.jxqingtuan.cn/pub/vol/volClass/current?'
# 我们要发起post请求的url
post_url = 'http://www.jxqingtuan.cn/pub/vol/volClass/join?'

# 获取青年大学习id
id_info = requests.get(info_url, headers=headers)
# 内容是json文件的格式，所以使用json库获取id
course = "%s" % json.loads(id_info.text.replace('\'', '\"'))['result']['id']

# 所属组织编号
nid = input("所属组织编号:")
# # 备注（可选）
# Org = input("备注:")
# 读取姓名文件实现批量刷记录
with open("name_list.txt", 'r', encoding='utf-8') as f:
    name_list = f.readlines()
for name in name_list:
    # 构建data
    data = {
        'course': f"{course}",
        'subOrg': '',
        'nid': f"{nid}",
        'cardNo': f"{name}"
    }
    # 发起post请求
    pos = requests.post(post_url, headers=headers, json=data)
    # # 状态码为[200]表示成功
    # print(pos)
    print(f"{name}\t成功")
    time.sleep(1)
