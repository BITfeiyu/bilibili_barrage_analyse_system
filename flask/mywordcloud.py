import jieba
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from wordcloud import WordCloud


def do_wordcloud(bv):
    text = open('data/barrage_' + bv + '.txt', 'r', encoding='utf-8').read()
    text = text.replace('\n', '').replace('\u3000', '')
    text_cut = jieba.lcut(text)
    text_cut = ' '.join(text_cut)
    # key_words = analyse.extract_tags(sentence=text_cut,topK=10,withWeight=True,allowPOS=())
    # print(key_words)

    # 过滤一些没有关系的词
    stop_words = ['“', '，', ' ', '我', '的', '是', '了',
                  '：', '？', '！', '啊', '你', '吗', '。', '我们']

    # background = Image.open("data/bilibili.jpg")
    # graph = np.array(background)

    word_cloud = WordCloud(font_path='simsun.ttc',
                           background_color='white',
                           collocations=False,
                        #    mask=graph,  # 指定词云的形状
                           stopwords=stop_words)

    word_cloud.generate(text_cut)
    plt.subplots(figsize=(12, 8))
    plt.imshow(word_cloud)
    plt.axis('off')
    # plt.show()
    word_cloud.to_file('data/wordcloud_' + bv + '.png')
