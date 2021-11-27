import re
from flask import Flask
from flask import request
from flask_cors import CORS
import json
import crawler as my_crawler
import mywordcloud as my_wordcloud
import moodanalyse as my_analyse

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/user/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.json.get("username")
        password = request.json.get("password")
        if username == "admin" and password == "admin":
            result = json.dumps(
                {'code': 0, 'message': 'Login success.', 'data': None})
        else:
            result = json.dumps(
                {'code': -1, 'message': 'Login failed.', 'data': None})
        return result


@app.route("/data/bv", methods=['POST', 'GET'])
def get_video_title():
    if request.method == 'POST':
        bv = request.json.get("bv")
        if bv == "":
            result = json.dumps(
                {'code': -1, 'message': 'BV should not be null.', 'data': None})
            return result
        else:
            title = my_crawler.get_video_data(bv)
            if title != None:
                # get_barrage = my_crawler.get_barrage_data(bv)
                # if get_barrage != None:
                #     result = json.dumps({'code':0, 'message':'Barrage crawled.', 'data':{'title': title}})
                #     return result
                result = json.dumps(
                    {'code': 0, 'message': 'BV received.', 'data': {'title': title}})
                return result


@app.route("/data/barrage", methods=['POST', 'GET'])
def get_barrage_data():
    if request.method == 'POST':
        bv = request.json.get("bv")
        if bv == "":
            result = json.dumps(
                {'code': -1, 'message': 'BV should not be null.', 'data': None})
            return result
        else:
            title = my_crawler.get_video_data(bv)
            get_barrage = my_crawler.get_barrage_data(bv)
            if get_barrage != None and title != None:
                result = json.dumps({'code': 0, 'message': 'Barrage crawled.', 'data': {
                                    'title': title, 'leng': get_barrage}})
                return result
            else:
                result = json.dumps(
                    {'code': -1, 'message': 'Barrage crawl failed.', 'data': None})
                return result


# 默认词云图的存储位置
default_image_path = "data/bilibili.png"


def get_image_stream(image_path=default_image_path):
    # import base64
    # image_stream = ''
    # with open(image_path, 'rb') as image_file:
    #     image_stream = image_file.read()
    #     image_stream = base64.b64encode(image_stream).decode()
    # return image_stream
    import io
    import PIL.Image as Image
    with open(image_path, 'rb') as image_file:
        image_stream = image_file.read()
    image_stream = Image.open(io.BytesIO(image_stream))

    image_byte_arr = io.BytesIO()
    image_stream.save(image_byte_arr, format="PNG")
    image_byte_arr = image_byte_arr.getvalue()
    return image_byte_arr


@app.route("/wordcloud", methods=['POST', 'GET'])
def get_wordcloud():
    if request.method == 'POST':
        bv = request.json.get("bv")
        if bv == "":
            result = json.dumps(
                {'code': -1, 'message': 'BV should not be null.', 'data': None})
            return result
        else:
            my_wordcloud.do_wordcloud(bv)
            # result = json.dumps({'code':0, 'message':'Wordcloud generated.', 'data':get_image_stream()})
            result = get_image_stream('data/wordcloud_' + bv + '.png')
            return result


@app.route("/moodAnalyse", methods=['POST', 'GET'])
def get_mood_analyse():
    if request.method == 'POST':
        bv = request.json.get("bv")
        if bv == "":
            result = json.dumps(
                {'code': -1, 'message': 'BV should not be null.', 'data': None})
            return result
        else:
            data = my_analyse.mood_analyse(bv)
            result = json.dumps(
                {'code': 0, 'message': 'Moodanalyse done.', 'data': data})
        return result


if __name__ == "main":
    app.run()
