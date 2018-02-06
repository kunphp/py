# -*- coding: utf-8 -*-
# @Author: Wykun
# @Date:   2018-01-19 14:09:03
# @Last Modified by:   Wykun
# @Last Modified time: 2018-02-06 16:29:07
# 根据文本内容生成词云图

import jieba    #分词库
import matplotlib.pyplot as plt    #数学绘图库
from wordcloud import WordCloud    #词云库

#读入txt内容
text = open(r'shuoshuo.txt','r',encoding='UTF-8').read()
#jieba分词

cut_text = jieba.cut(text)
result = '/'.join(cut_text)#必须给个符号分隔分词结果成字符串

#3.font_path 字体 生成词云wordcloud不支持中文，需要有中文字体库
#width、height 指定生成词云图的像素大小，默认背景颜色为黑色,统一文字颜色：mode='RGB' 
#background_color="white", 背景颜色
#max_words=2000,# 词云显示的最大词数
#mask=alice_coloring,#设置背景图片
wc = WordCloud(font_path=r"C:\Windows\Fonts\STZHONGS.TTF",background_color='white',width=800,height=600,max_font_size=120,max_words=500,min_font_size=10,mode='RGB',random_state=42)
wc.generate(result)
wc.to_file(r"bible.png");#保存词云图

plt.figure('词云图')#指定所绘图名称
plt.imshow(wc)# 以图片的形式显示词云
plt.axis('off')#关闭图像坐标系
plt.show()#显示词云图
