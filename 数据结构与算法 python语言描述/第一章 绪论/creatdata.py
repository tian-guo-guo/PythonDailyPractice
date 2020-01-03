'''
建立一个表，其中包含从0到10000*n-1的整数值
'''
def test1(n):
    lst = []
    for i in range(n*10000):
        lst = lst + [i]
    return lst

def test2(n):
    lst = []
    for i in range(n*10000):
        lst.append(i)
    return lst 

def test3(n):
    return [i for i in range(n*10000)]

def test4(n):
    return list(range(n*10000))