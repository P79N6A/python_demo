import jieba

f = open("threekingdoms.txt", 'r', encoding='utf-8')
txt = f.read()
f.close()
for c in '!,.:|?;#$@%^&*()-_+=\\/<>`~{}[]。：；，？"':
    txt = txt.replace(c, "")
excludes = {'将军', '却说', '二人', '不可', '如此', '不能','不能','不敢','主公','荆州','如何','商议','大喜','今日','军士','军马','左右','次日','东吴','天下','引兵'}
# 生成一个list
name = jieba.lcut(txt)
counts = {}
for str in name:
    if len(str) == 1:
        continue
    else:
        if str in ['玄德曰', '玄德']:
            rword = '刘备'
        elif str in ['孔明曰', '孔明']:
            rword = '诸葛亮'
        elif str in ['丞相', '孟德', '孟德曰']:
            rword = '曹操'
        elif str in ['关公']:
            rword = '关羽'
        else:
            rword = str
        counts[rword] = counts.get(rword, 0) + 1
for word in excludes:
    del counts[word]
ls = list(counts.items())
ls.sort(key=lambda x: x[1], reverse=True)
for i in range(5):
    word, count = ls[i]
    print("{0:<10}{1:>5}".format(word, count))
