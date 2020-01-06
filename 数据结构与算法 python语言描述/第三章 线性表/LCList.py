class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

class LinkedListUnderflow(ValueError):
    pass

class LCList:       # 循环单链表类
    def __init__(self):
        # 这种表对象只需一个数据域_rear，它在逻辑上始终引用着表的尾结点。
        self._rear = None
    def is_empty(self):
        return self._rear is None 
    def prepend(self, elem):        # 前端插入
        p = LNode(elem)
        if self._rear is None:
            p.next = p      # 建立一个结点的环
            self._rear = p 
        else: 
            p.next = self._rear.next 
            self._rear.next = p 
    def append(self, elem):     # 尾端插入
        self.prepend(elem)
        self._rear = self._rear.next 
    def pop(self):      # 前端弹出
        if self._rear is None:
            raise LinkedListUnderflow('in pop of CLList')
        p = self._rear.next 
        if self._rear is p: 
            self._rear = None 
        else:
            self._rear.next = p.next 
        return p.elem 
    def printall(self):     # 输出表元素
        if self.is_empty():
            return 
        p = self._rear.next 
        while True: 
            print(p.elem)
            if p is self._rear:
                break
            p = p.next 


mlist1 = LCList()
for i in range(10):
    mlist1.prepend(i)
for i in range(11, 20):
    mlist1.append(i)
mlist1.printall()