import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from snownlp import SnowNLP

# 将txt转换成csv格式


def txt_to_csv(bv):
    import csv
    out = open('data/barrage_'+bv+'.csv', 'w', encoding='utf-8', newline='')
    csv_writer = csv.writer(out, dialect='excel')
    f = open('data/barrage_'+bv+'.txt', 'r', encoding='utf-8')
    index = 1
    csv_writer.writerow(['id', 'content'])
    for line in f.readlines():
        line = line.replace('\n', '')
        newline = [index, line]
        index = index + 1
        csv_writer.writerow(newline)


def mood_analyse(bv):
    txt_to_csv(bv)
    data = pd.read_csv('data/barrage_' + bv + '.csv')
    emotion_data = data[['id', 'content']]
    # emotion_data = emotion_data.head(10)
    emotion_data['emotion'] = emotion_data['content'].apply(
        lambda x: SnowNLP(x).sentiments)
    # data2 = (emotion_data[emotion_data['emotion'] < 0.4])
    # data2 = data2.head()
    # print(data2)

    # 绘制直方图
    hist_x = ['0.0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9']
    hist_y = []
    for index in range(0, 10):
        hist_y.append(float(emotion_data[(emotion_data.emotion >= 0.1*index) &
                                         (emotion_data.emotion < 0.1*(index+1))].id.count()))
    hist_data = {'x': hist_x, 'y': hist_y}

    # 绘制饼图
    pie_pos = 0
    for num in hist_y[5:]:
        pie_pos = pie_pos + num
    # pie_pos = emotion_data[emotion_data.emotion >= 0.5].id.count()
    pie_neg = emotion_data.shape[0] - pie_pos
    # pie_data = {'pos': float(pie_pos), 'neg': float(pie_neg)}
    pie_data = [{'value': float(pie_pos), 'name': 'positive'},
                {'value': float(pie_neg), 'name': 'negaive'}]

    return {'pie_data': pie_data, 'hist_data': hist_data}

    # emotion_data = emotion_data.head()

    # emotion_data = emotion_data.describe()

    # pos,neg = 0,0
    # for  i in emotion_data['emotion']:
    # 	if i >= 0.5:
    # 		pos += 1
    # 	else:
    # 		neg += 1
    # print(f'积极弹幕数据为：{pos}' + '\n' + f'消极弹幕数据为：{neg}')
    # plt.rcParams['font.sans-serif'] = ['SimHei']
    # plt.rcParams['axes.unicode_minus'] = False
    # pie_labels = 'positive','negative'
    # plt.pie([pos,neg],labels=pie_labels,autopct='%1.2f%%',shadow=True)
    # plt.show()

    # plt.rcParams['font.sans-serif'] = ['SimHei']
    # plt.rcParams['axes.unicode_minus'] = False

    # bins = np.arange(0, 1.1, 0.1)  # 设置区间
    # plt.hist(emotion_data['emotion'], bins, color='#4F94CD', alpha=0.9)
    # plt.xlim(0, 1)
    # plt.xlabel('情感分析')
    # plt.ylabel('数量')
    # plt.title('EDG夺冠弹幕数据情感分析直方图')
    # plt.show()


# txt_to_csv("BV1hD4y1X7Rm")
