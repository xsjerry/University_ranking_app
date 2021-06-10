import requests
import json

def get_data(year):
    url = "https://www.shanghairanking.cn/api/pub/v1/arwu/rank"

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }

    params = {
        'year' : year,
    }
    response = requests.get(url,headers=header,params=params)
    result = response.text
    result = json.loads(result)["data"]["rankings"]


    l = []
    for i in result[0:100]:
        t = [i['univNameCn'], i['region'], i['regionRanking']]
        l.append(t)

    return l


