# 列表
ls = [["a", "b"], ["cd"], ["ef"]]
for row in range(len(ls)):  # 获得行数
    for col in range(len(ls[row])):  # 获得对应行数的list的长度
        print(ls[row][col])


dict = {"a":1,"b":2,"c":3}

val = dict.values()

print(val)


for i in val:
    print(i)
