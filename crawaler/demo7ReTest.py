import  re


# demo0 .
match = re.search(r'[\d.]*',"我是123.445")
if match:
    print(match.group(0))
# demo1 search函数  搜索能匹配字符串的第一个位置
match = re.search(r'[1-9]\d{5}',"BIT1000814")
# if match:
#     print(match.group(0)) # 输出100081

# demo2 match函数  从字符串的开始位置匹配

match = re.match(r'[1-9]\d{5}',"1000814 BIT")  # BIT 100081 不会返回任何的结果
# if match: # 输出100081
#     print(match.group(0))


# demo3 findall 以列表类型返回所有的匹配字符串
ls = re.findall(r'[1-9]\d{5}',"1000814 BIT 100082")
# print(ls) ['100081','100082']

# demo4 split
ls = re.split(r'[1-9]\d{5}',"TIN1000814 BIT 100082")
# print(ls) ['TIN', '4 BIT ', '']

# demo5 finditer
iter = re.finditer(r'[1-9]\d{5}',"1000814 BIT 100082")
# for i in iter:
#     if i:
#         print(" "+i.group(0)+" "+str(i.span()))
# demo6 sub
str = re.sub(r'[1-9]\d{5}','Y',"1000814 BIT 100082",2)
# print(str) #Y4 BIT Y

# demo7 最小匹配和贪婪匹配  贪婪匹配匹配最长的字符串
match = re.search(r'PY.*?N',"PYNPYNNN") # 以PY开头 N结尾的所有字符串
# print(match.group(0)) 贪婪PYNPYNNN  最小PYN