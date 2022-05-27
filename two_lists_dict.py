keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]


dic = dict()

for i in range(len(keys)):
    dic.update({keys[i]: values[i]})
print(dic)