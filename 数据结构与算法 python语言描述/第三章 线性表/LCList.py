class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

class LinkedListUnderflow(ValueError):
    pass

class LCList:       # 循环单链表类
    def __init__(self):
        # 单链表的变形循环单链表，最后一个结点的next域不用None，而是指向表的第一个结点
        # 这样可以同时支持O(1)时间的表头/表尾插入 和 O(1)时间的表头删除。
        # 循环单链表操作和普通单链表的差异就在于扫描循环的结束控制。
        # 这种表对象只需一个数据域_rear，它在逻辑上始终引用着表的尾结点。
        # 前端加入结点，就是在尾结点和首结点之间加入新的首结点，尾结点引用不变，
        # 尾端加入新结点，需要更新尾结点引用。
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