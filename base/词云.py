# encoding = utf-8
import wordcloud
import jieba
# from scipy.misc import imread

# mask = imread('1.png')
# f = open("新时代中国特色社会主义.txt", "r", encoding='utf-8')
# txt = f.read()
# f.close()
txt1="有道翻译提供即时免费的中文、英语、日语、韩语、\
法语、德语、俄语、西班牙语、葡萄牙语、越南语、\
印尼语全文翻译、网页翻译、文档翻译服务。"
ls = jieba.lcut(txt1)
wl = " ".join(ls)
w = wordcloud.WordCloud(font_path="Hiragino Sans GB.ttc", width=1000, height=700, background_color="black",
                        max_words=15)
w.generate(wl)
w.to_file("grwordcloud.png")
