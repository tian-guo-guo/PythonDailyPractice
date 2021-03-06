'''
数据类型和数据构造
处理有理数，用两个整数表示一个有理数，分别表示分子和分母
eg:3/5，存入变量为a1 = 3, b1 = 5
利用python函数可返回多对象元组和多项赋值的机制，加法函数定义如下：
'''

# try 1:
a1 = 3
b1 = 5
def rational_plus(a1, b1, a2, b2):
    num = a1*b2 + b1*a2
    den = b1*b2 
    return num, den 

a2, b2 = rational_plus(a1, b1, 7, 10)
print(a2, b2)

# 如果真这样写程序，很快就会遇到非常麻烦的管理问题:编程者需要时时记住哪两个变量
# 记录的是一个有理数的分子和分母，操作时不能混淆不同的有理数如果需要换一个有理数
# 参与运算，也会遇到成对变量名的代换问题。程序比较复杂时，做这类事情很容易出错，
# 而如果真发现程序有错误，确定错误的位置和更正也将极其费时费力。总而言之，用独立
# 的分别存在的两个整数表示一个有理数，这种技术完全不可取。

# try 2:
# 利用数据组合机制，用一个元组表示一个有理数，第0项表示分子，第1项表示分母
r1 = (3, 5)
r2 = (7, 10)
def rational_plus(r1, r2):
    num = r1[0]*r2[1] + r2[0]*r1[1]
    den = r1[1]*r2[1]
    return num, den  
n, d = rational_plus(r1, r2)
print(n, d, end=' ')