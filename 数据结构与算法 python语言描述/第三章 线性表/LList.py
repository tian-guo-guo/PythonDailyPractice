class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

class LinkedListUnderflow(ValueError):
    pass 

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
            print(p.elem, end = '')
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

mlist1 = LList()
for i in range(10):
    mlist1.prepend(i)
for i in range(11, 20):
    mlist1.append(i)
mlist1.printall()
for x in mlist1.elements():
    print(x)