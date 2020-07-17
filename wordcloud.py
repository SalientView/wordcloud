import pylab as mpl     #import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
## 加载数据包
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import jieba
import seaborn as sns
import nltk

stop_words = pd.read_csv("stop_words.txt",header=None,names = ["stop_words"])
text = pd.read_csv('text.csv')

def words_cut(s):
    cutword = pd.Series(list(jieba.cut(s)))[pd.Series(list(jieba.cut(s))).apply(len)>1]
    cutword = cutwords[~cutword.isin(stop_words)]
    return cutwors.values
    
text['分词'] = text['content'].apply(words_cut)

# 词云图
from wordcloud import WordCloud
plt.figure(figsize=(10,5))
wordcloud = WordCloud(font_path='C:/Software/Anaconda3/Lib/site-packages/wordcloud/SimHei.ttf',  # 此处根据自己本地位置设置
                      margin=5, width=1800, height=900,
                      background_color="white")
wordcloud.generate("/".join(np.concatenate(text['分词'])))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

# 词频统计
words = np.concatenate(text['分词'])
words = pd.DataFrame({"word":words})
word_frequency = words.groupby("word").size().sort_values(ascending=False)
top = word_frequency[:20]

fig,ax = plt.subplots(figsize=(12,6))
ax = top.plot(kind = 'bar',rot=0,width=0.75,color=sns.color_palette('winter_d',n_colors=20))
for i,j in zip(np.arange(20),top):
    ax.text(i,j/2,j,color='white',ha='center')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.set_yticks([])
ax.set_xlabel('')
plt.show()

