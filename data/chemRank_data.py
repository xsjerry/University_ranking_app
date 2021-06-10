import requests
import json

def get_cnData():
    url = "https://www.shanghairanking.cn/api/pub/v1/bcsr/rank"
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    params = {
        'target_yr': '2020',
        'yr': '2019',
        'subj_code': '0703',
    }

    response = requests.get(url, headers = header, params=params)
    result = json.loads(response.text)
    result = result['data']['rankings']

    l = []
    for i in result[0:30]:
        data = [i["univNameCn"], i['rankPctTop']]
        l.append(data)

    return l

def get_worldData():
    url = " https://www.shanghairanking.cn/api/pub/v1/gras/rank"
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    params = {
        'year': '2021',
        'subj_code': 'RS0103',
    }

    response = requests.get(url, headers = header, params=params)
    result = json.loads(response.text)['data']['rankings']

    l = []
    for i in result[0:30]:
        data = [i['univNameCn'], i['region']]
        l.append(data)

    return l


