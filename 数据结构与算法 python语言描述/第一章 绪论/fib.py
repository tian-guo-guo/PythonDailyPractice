'''
F0=F1=1
Fn=Fn-1+Fn-2,对于n＞1
'''

# method 1：递归算法
def fib(n):
    if n<2:
        return 1 
    else:
        return fib(n-1) + fib(n-2)
# 计算Fn的时间代价（考虑求加法操作的次数）大致等于计算Fn-1和Fn-2的时间代价之和。
# 计算Fn的事假代价大致等比于斐波那契数Fn的值。
# limn→∞=((sqrt(5)+1)/2)^n，约等于1.618，所以计算Fn的时间代价按n值的指数增长。

# method 2：递推算法：
def fib(n):
    f1 = f2 = 1 
    for k in range(1, n):
        f1, f2 = f2, f2 + f1 
    return f2 
# 用这个算法计算Fn的值，循环前工作只做一次，循环需要做n-1次
# 每次循环中只执行了几个简单动作，总的工作量（基本操作执行次数）与n值呈某种线性关系
