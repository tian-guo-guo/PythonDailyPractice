from random import randint

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

# 新类的基本使用形式与LList相同，变化的只是后端插入操作的效率。
mlist1 = LList1() 
mlist1.prepend(99)
for i in range(11, 20):
    mlist1.append(randint(1, 20))
for x in mlist1.filter(lambda y:y%2==0):
    print(x)

'''
类设计的内在一致性
    现在结合上面的例子，简单讨论类设计中的一个重要原则。
    一个类定义是一个整体，它描述了一种程序对象。类定义比较复杂，其中可以有许多
成分，特别是可能定义了许多方法。每个方法定义是类定义中的一个独立片段，编程语言
( Python)对不同方法之间的关系并没有任何约束，也不对这样-组方法定义做任何相互关系方
面的检查。但是，作为同一个类定义的成分，这些方法需要相互协调，保持-致， 才能保证所
定义的程序对象有意义。这件事需要编程序的人考虑和保证。
    以类LList1为例，前面讨论了两种可能设计: -种设计要求在表空的时候_ head 和
_rear的值都是None,另一种设计只要求这时_ head 为None。基于两种设计都能正确实现
这个类，但是-旦选定了一种设计，类中的所有方法都必须遵照这种设计来定义，包括所有的
插人和删除操作。
    -般情况，在设计-个类时总需要考虑一套统一的规则。 类的初始化方法建立起的对象应
满足这些规则，操作也不能破坏规则，这样定义的类才是有效的。
    当然，不同规则可能影响类定义的细节和复杂程度。在上面例子里采用了后一种设计， 也
是因为它更简单，需要维护的关系少-点。还考虑到基类的已有设计，尽可能与其保持-致,
以便更多地利用已有的功能。
'''
