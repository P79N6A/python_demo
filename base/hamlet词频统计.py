f = open("hamlet.txt", 'r')
s = f.read()
s = s.lower()
f.close()
# 特殊字符替换为空格
for c in "!,.:|?';#$@%^&*()-_+=\\/<>`~{}[]":
    s = s.replace(c, " ")
counts = {}
# 字符串根据空格分隔为一个list
words = s.split()
# 词频统计
for word in words:
    counts[word] = counts.get(word, 0) + 1
# 字典转换为列表
ls = list(counts.items())
# 将列表排序
ls.sort(key=lambda x: x[1], reverse=True)
for l in range(10):
    word, count = ls[l]
    print("{0:<10}{1:>5}".format(word, count))
