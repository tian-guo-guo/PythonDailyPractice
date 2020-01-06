from random import randint

class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

class LinkedListUnderflow(ValueError):
    pass

class DLNode(LNode):        # 双链表结点类
    def __init__(self, elem, prev=None, next_=None):
        LNode.__init__(self, elem, next_)
        self.prev = prev 

class LList:
    # LList类的定义，初始化函数和简单操作
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    def pop(self):
        if self._head is None:      # 无结点，引发异常
            raise LinkedListUnderflow('in pop')
        e = self._head.elem
        self._head = self._head.next
        return e
    # 后端操作

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    def pop_last(self):
        if self._head is None:      # 空表
            raise LinkedListUnderflow('in pop_last')
        p = self._head
        if p.next is None:          # 表中只有一个元素
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:  # 直到p.next是最后结点
            p = p.next
        e = p.next.elem
        p.next = None
        return e
    # 其他操作

    def find(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next

    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(', ', end='')
            p = p.next
        print('')
    # proc是可以作用于表元素的操作函数，它被作用于每个表元素
    # eg:list1.foreach(print)

    def for_each(self, proc):
        p = self._head
        while p is not None:
            proc(p.elem)
            p = p.next

    def elements(self):
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    def filter(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next

# LList的一个缺点是只能在尾端插入，效率太低，现在在尾结点后也加入一个引用域，
# 只需常量时间就能尾结点O(1)
# 因前面LList已经实现很多功能，所以直接继承就可以了

class LList1(LList):
    def __init__(self):
        # 初始化应该包括LList对象的所有数据域，
        # 所以最合理且方便的方式就是对self对象调用LList类的初始化函数
        LList.__init__(self)
        # 初始化一个尾结点引用域
        self._rear = None

    # 前端插入操作，重写父类方法
    def prepend(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:      # 是空表
            self._head = LNode(elem, self._head)

    # 增加尾结点之后，append方法也要重写
    def append(self, elem):
        if self._head is None:      # 是空表
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next

    # 弹出元素的重写，因为删除尾结点之后还需要更新_rear
    def pop_last(self):
        if self._head is None:      # 是空表
            raise LinkedListUnderflow('in pop_last')
        p = self._head
        if p.next is None:          # 表中只有一个元素
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:  # 直到p.next是最后结点
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        return e

# 定义一个双链表类，从带首尾结点引用的单链表类LList1派生
class DLList(LList1):       # 双链表类
    def __init__(self):
        LList1.__init__(self)
    def prepend(self, elem):
        p = DLNode(elem, None, self._head)
        if self._head is None:  # 空表
            self._rear = p 
        else:       # 非空表，设置prev引用
            p.next.prev = p 
        self._head = p 
    def append(self, elem):
        p = DLNode(elem, self._rear, None)
        if self._head is None:      # 空表插入
            self._head = p 
        else:       # 非空表，设置next引用
            p.prev.next = p 
    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop of DLList')
        e = self._head.elem
        self._head = self._head.next
        if self._head is not None:  # _head空时不需要做任何事
            self._head.prev = None 
        return e  
    def pop_last(self):
        if self._head is None: 
            raise LinkedListUnderflow('in pop_last of DLList')
        e = self._rear.elem
        self._rear = self._rear.prev
        if self._rear is None:      
            self._head = None       # 设置_head保证is_empty正确工作
        else:
            self._rear.next = None 
        return e  

# 新类的基本使用形式与LList相同，变化的只是后端插入操作的效率。
# 从代码执行的输出结果上看不到什么不同，只是有些操作的性能改善了。
mlist1 = DLList()
mlist1.prepend(99)
for i in range(11, 20):
    mlist1.append(randint(1, 20))
for x in mlist1.filter(lambda y: y % 2 == 0):
    print(x)
mlist1.printall()