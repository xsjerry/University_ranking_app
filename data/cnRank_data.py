import requests
import json

def get_data(year):
    url = "https://www.shanghairanking.cn/api/pub/v1/bcur"

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }

    params = {
        'bcur_type': '11',
        'year': year,

    }

    response = requests.get(url, headers=header, params=params)
    result = response.text  # 此时获得的输出是str类型
    result = json.loads(result)  # 将其转化为字典dict类型
    result = result["data"]["rankings"]  # 获得自己想要的元素

    l = []

    for i in result[0:50]:
        t = [i["univNameCn"], i["univCategory"], ' '.join(i["univTags"]), i["province"]]
        l.append(t)

    return l