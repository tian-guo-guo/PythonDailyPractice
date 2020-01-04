'''
采用super函数而不直接写具体基类的名字，产生的查找过程更加灵活。
如果直接写基类的名字，无论在什么情况下执行，总是调用该基类的方法，而如果写super()，
Python解释器将根据当前类的情况去找到相应的基类，自动确定究竟应该使用哪个基类的属性。
'''
class C1:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
    def m1(self):
        print(self.x, self.y)

class C2(C1):
    def m1(self):
        super().m1()
        print('Somne special service.')

c2 = C2(3, 4)
res = c2.m1()
print(res)
