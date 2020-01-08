class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

class LinkedListUnderflow(ValueError):
    pass 

# 基于结点类LNode定义一个单链表
class LList:
    # LList类的定义，初始化函数和简单操作
    def __init__(self):
        # 只有一个引用链接结点_head域，初始化为None表示建立的是一个空表
        # _head域作为对象的内部表示，不希望外部使用
        self._head = None 
    # 判断表空的操作检车_head
    def is_empty(self):
        return self._head is None 
    # 表头插入元素
    def prepend(self, elem):
        self._head = LNode(elem, self._head)
    # 操作pop删除表头结点并返回这个结点里的数据
    def pop(self):
        if self._head is None:      # 无结点，引发异常
            raise LinkedListUnderflow('in pop')
        e = self._head.elem 
        self._head = self._head.next 
        return e  
    # 后端操作，在链表最后插入元素，必须先找到链表最后一个结点
    # 先扫描循环，找到相应结点后把包含新元素的结点插入在其后
    def append(self, elem):
        # 分两种情况，如果原表为空，引用新结点就该是表对象的_head域，
        # 否则就是已有最后结点的next域
        if self._head is None:
            self._head = LNode(elem)
            return 
        p = self._head
        while p.next is not None:
            p = p.next 
        p.next = LNode(elem)
    # 删除最后结点，必须先找到它的前一结点，也就是倒数第二个结点，
    # p.next.next为None的p，不仅删去最后元素，还把它返回（与pop统一）
    def pop_last(self):
        # 在开始一般性扫描之前，需处理两个特殊情况
        # 1. 表空时引发异常
        # 2. 只有一个元素时，取出元素后应修改头指针
        # 3. 一般情况是找到倒数第二个结点
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
    # 找打满足给定条件的表元素，pred是一个判断谓词，返回第一个满足谓词的表元素
    # 这个操作也需要采用扫描模式
    def find(self, pred):
        p = self._head
        while p is not None: 
            if pred(p.elem):
                return p.elem 
            p = p.next 
    # 打印/查看所有表情况
    def printall(self):
        p = self._head 
        while p is not None: 
            print(p.elem, end = '')
            if p.next is not None: 
                print(', ', end='')
            p = p.next 
        print('')
    # proc是可以作用于表元素的操作函数，它被作用于每个表元素
    # eg:list1.foreach(print)，规范但不够灵活，常使用lambda
    def for_each(self, proc):
        p = self._head
        while p is not None:
            proc(p.elem)
            p = p.next 
    # 定义迭代器
    def elements(self):
        p = self._head 
        while p is not None:
            yield p.elem 
            p = p.next 
    # 筛选生成器
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