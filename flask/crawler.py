import requests
import chardet
import json
import re


def get_api_data(url):
    try:
        response = requests.get(url, timeout=None)
        if response is not None:
            response.encoding = chardet.detect(response.content)['encoding']
            return response.text
        else:
            return None
    except Exception as e:
        print(e.args)


def get_video_data(bv):
    try:
        url = 'https://api.bilibili.com/x/web-interface/view?bvid=' + bv + '&jsonp=jsonp'
        json_data = json.loads(get_api_data(url))
        title = json_data['data'].get('title')
        return title
    except Exception as e:
        print(e.args)


def get_barrage_data(bv):
    try:
        leng = 0
        url = 'https://api.bilibili.com/x/player/pagelist?bvid=' + bv + '&jsonp=jsonp'
        json_data = json.loads(get_api_data(url))
        base_api = 'http://api.bilibili.com/x/v1/dm/list.so?oid='
        all_api = []
        for cid_datas in json_data['data']:
            cid = cid_datas.get('cid')
            detail_api = base_api + str(cid)
            all_api.append(detail_api)
        for detail_api in all_api:
            barrage_data = get_api_data(detail_api)
            barrage_data = re.findall('<d.*?>(.*?)</d>', barrage_data, re.S)
            with open('data/barrage_' + bv + '.txt', 'a', encoding='utf-8') as f:
                for barrage in barrage_data:
                    f.write(barrage + '\n')
                leng = leng + len(barrage_data)
        return leng
    except Exception as e:
        print(e.args)
