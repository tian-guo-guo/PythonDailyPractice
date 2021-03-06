'''
ADT List:                   #一个表抽象数据类型
    List(self)              #表构造操作，创建一个新表
    is_ empty(self)         #判断self是否为-一个空表
    len(self)               #获得self的长度
    prepend(self, elem)     # 将元素elem加人表中作为第一个元素
    append(self, elem)      # 将元素elem加入表中作为最后- -个元素
    insert(self, elem, i)   # 将elem加入表中作为第i个元素，其他元素的顺序不变
    del_ first(self)        #删除表中的首元素
    del_ last(self)         #删除表中的尾元素
    del(self, i)            #删除表中第i个元素
    search(self, elem)      #查找元素elem在表中出现的位置，不出现时返回-1
    forall(self, op)        #对表中的每个元素执行操作op
'''

'''
Python标准类型list就是一种元素个数可变的线性表，可以加入和删除元素，在各种操作
中维持已有元素的顺序。其重要的实现约束还有:
●基于下标(位置)的高效元素访问和更新，时间复杂度应该是0(1)。,
●允许任意加入元素(不会出现由于表满而无法加入新元素的情况)，而且在不断加入元
素的过程中，表对象的标识(函数id得到的值)不变。

这些基本约束决定了list 的可能解决方案:
●由于要求0(1)时间的元素访问，并能维持元素的顺序，这种表只能采用连续表技术，
表中元素保存在-块连续存储区里。
●要求能容纳任意多的元素，就必须能更换元素存储区。要想在更换存储区时list对象的
标识(id)不变，只能采用分离式实现技术。
'''

'''
一些主要操作的性质：
●len(.) 是0(1)操作，因为表中必须记录元素个数，自然可以简单地取用。
●元素访问和赋值，尾端加入和尾端删除(包括尾端切片删除)都是0(1)操作。
●一般位置的元素加入、切片替换、切片删除、表拼接( extend) 等都是O(n)操作。pop
操作默认为删除表尾元素并将其返回，时间复杂度为0(1)，一般情况的pop操作(指定
非尾端位置)为O(n)时间复杂度。
'''

# 时间复杂度为O(n)
def reverse(self):
    elems = self.elements
    i, j = 0, len(elems)-1
    for i < j:
        elems[i], elems[j] = elems[j], elems[i]
        i, j = i+1, j-1


'''
思路：
1. 复制一份列表
2. 定义首尾i, j的下标索引
3. 当i<j时：
        首尾交换
        下标加一
'''

# 完整函数
def reverse(l):
    li = l
    i, j = 0, len(li)-1
    for _ in range(len(li)):
        if i < j:
           li[i], li[j] = li[j], li[i]
           i, j = i+1, j-1
    return li


print(reverse([1, 2, 3, 4, 5, 6, 7, 8]))