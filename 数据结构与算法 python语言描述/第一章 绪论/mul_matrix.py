'''
矩阵乘法：
求出两个n*n矩阵m1和m2的乘积，存入另一个n*n矩阵m。
'''

import numpy as np


def mul_matrix(n, m1, m2):
    m = np.array([[0]*n]*n)
    for i in range(n):
        for j in range(n):
            x = 0.0
            for k in range(n):
                x = x + m1[i][k] * m2[k][j]
            m[i][j] = x
    return m


m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
print(mul_matrix(3, m1, m2))

'''
时间复杂度：
T(n) = O(n) * O(n) * (O(1) + O(n) * O(1) + O(1))
     = O(n) * O(n) * O(n)
     = O(n * n * n)
     = O(n^3)
'''