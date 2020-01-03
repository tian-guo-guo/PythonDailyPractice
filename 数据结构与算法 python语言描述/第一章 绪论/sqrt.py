'''
求平方根（牛顿迭代法）：
0. 对给定正实数x和允许误差e，令变量y取任意正实数值，如令y=x;
1. 如果y*y与x足够接近，即|y*y-x|<e，计算结束并把y作为结果；
2. 取z=(y+x/y)/2;
3. 将z作为y的新值，回到步骤1.
'''
def sqrt(x):
    y = 1.0
    while abs(y*y-x)>1e-6:
        y = (y+x/y)/2
    return y 

print(sqrt(5))
