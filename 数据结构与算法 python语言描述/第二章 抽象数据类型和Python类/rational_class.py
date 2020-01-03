class Rational0:
    def __init__(self, num, den=1):
        self.num = num 
        self.den = den  
    def plus(self, another):
        den = self.den * another.den  
        num = (self.num * another.den + self.den * another.num)
        return Rational0(num, den)
    def print(self):
        print(str(self.num) + '/' + str(self.den))

r = Rational0(3, 7)
a = Rational0(4, 5)
p = r.plus(a)
pr = r.print() 
# print(r)
# print(p.print()) # 结果不是最简形式
# print(pr)

# 以上代码有两个问题
# 1. 最终结果不是最简形式，所以需要定义一个求最大公约数的函数gcd
#    因为它的第一参数不用传self，所以要定义成静态方法@staticmethod
#    令外，gcd属于Rational里的局部函数，所以gcd是有理数类里定义的一个实例方法
# 2. 有理数类的初始化方法没有检查参数，需要隐藏属性
class Rational:
    @staticmethod 
    def _gcd(m, n):
        if n == 0:
            m, n = n, m 
        while m != 0: 
            m, n  = n % m, m 
        return n 
    def __init__(self, num, den=1):
        # 检查参数的类型和分母的值，不满足要求抛出适当的异常
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError 
        if den == 0:
            raise ZeroDivisionError 
        sign = 1 
        # if语句提取有理数的符号，sign=1表示是整数，-1表示是负数
        if num < 0:
            num, sign = -num, -sign 
        if den < 0:
            den, sign = -den, -sign 
        g =  Rational._gcd(num, den)
        # call function gcd defined in this class.
        # 化简后的分子和分母设置有理数的数据属性
        self._num = sign * (num // g)
        self._den = den // g 

    # 定义一对解析操作(也是实例方法)，为的是不暴露属性
    def num(self):
        return self._num 
    def den(self):
        return self._den 
    
    # 更自然的方式实现(+ - * /)
    def __add__(self, another):     # mimic + operator 
        den = self._den * another.den() 
        num = (self._num * another.den() + self._den * another.num())
        return Rational(num, den)
    
    def __mul__(self, another):     # mimic + operator
        return Rational(self._num * another.num(), self._den * another.den())

    def __floordiv__(self, another):    # mimic // operator
        if another.num() == 0:
            raise ZeroDivisionError
        return Rational(self._num * another.den(), self._den * another.num())
    
    # 有理数相等、小于运算的方法定义
    def __eq__(self, another):
        return self._num * another.den() == self.den * another.num() 
    def __lt__(self, other):
        return self._num * another.den() < self._den * another.num()

    def __str__(self):
        return str(self._num) + '/' + str(self._den)
    
    def print(self):
        print(self._num, '/', self._den)

five = Rational(5)     # 初始化方法的默认参数保证用整数直接创建有理数
x = Rational(3, 5)
print(five)
print(x)
print(x.print())
print('Two thirds are', Rational(2, 3))
y = five + x * Rational(5, 17)
if y < Rational(123, 11):
    print('<')
t = type(five)
if isinstance(five, Rational):
    print(type)

'''
ADT Rational:                           #定义有理数的抽象数据类型
    Rational(self, int num, int den)    #构造有理数num/den
    + (self, Rational r2)               #求出本对象加r2的结果(有理数)
    一(self, Rational r2)               #求出本对象减r2的结果
    * (self, Rational r2)               #求出本对象乘以r2的结果
    /(self, Rational r2)                #求出本对象除以r2的结果
    num(self)                           #取得本对象的分子
    den(self)                           #取得本对象的分母
'''
