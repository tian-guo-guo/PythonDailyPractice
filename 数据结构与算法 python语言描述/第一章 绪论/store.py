'''
把得到的一系列数据存入一个表，其中得到一个数据是O(1)常量时间操作
'''
data = []
while data:
    x = data.pop()
    data.insert(0, x) # 把新数据加在表的最前面

# or
data = [] 
while data:
    x = data.pop()
    data.insert(len(data), x) # 新数据加在最后，或写data.append(x)

# 前一种程序段需要O(n2)，后一种程序段需要O(n)时间，造成这种情况与list的实现方式有关