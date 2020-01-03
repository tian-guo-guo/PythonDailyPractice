'''
编写一个Python函数 is_multiple(n, m)，用来接收两个整数值 n 和 m，
如果 n 是 m 的倍数，即存在整数 i 使得 n = mi，那么函数返回 True，否则返回 False
'''
def is_multiple(n, m):
    return True if n%m==0 else False 

res = is_multiple(10, 5)
print(res)

# or 

def is_multiple2(n, m):
    return n%m==0

res2 = is_multiple2(10, 5)
print(res2)
