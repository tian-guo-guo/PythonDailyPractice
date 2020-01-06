# 定义一个简单的表节点
class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem 
        self.next = next_ 

ilist1 = LNode(1)
p = ilist1
# 包含十个节点的单链表
for i in range(2, 11):
    p.next = LNode(i)
    p = p.next 
p = ilist1
while p is not None:
    print(p.elem)
    p = p.next

# # 表首端插入
# q = LNode(13)
# q.next = head.next 
# head = q 
# # 一般情况插入
# q = LNode(13)
# q.next = pre.next 
# pre.next = q 
# # 一般情况的元素删除
# pre.next = pre.next.next 
# # 扫描
# p = head 
# while p is not None and 还需要继续的其他条件:
#     p = p.next 
# # 按下标定位
# p = head 
# while p is not None and i > 0:
#     i -= 1 
#     p = p.next 
# # 按元素定位
# p = head 
# while p is not None and not pred(p.elem):
#     p = p.next 
# # 求表的长度
# def length(head):
#     p, n = head, 0 
#     while p is not None: 
#         n += 1 
#         p = p.next 
#     return n 