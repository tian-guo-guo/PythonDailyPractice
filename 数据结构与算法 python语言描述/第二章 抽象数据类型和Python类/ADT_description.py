'''
ADT Rational:                     #定义有理数的抽象数据类型
    Rational(int num, int den)    #构造有理数num/den
    十(Rational rl, Rational r2)  #求出表示rl十r2的有理数
    一(Rational r1, Rational r2)  #求出表示r1一r2的有理数
    *(Rational rl, Rational r2)   #求出表示r1*r2的有理数
    / (Rational r1, Rational r2)  #求出表示r1/r2的有理数
    num(Rational r1)              #取得有理数r1的分子
    den(Rational r1)              #取得有理数r1的分母
'''

'''
ADT Date:                               #定义日期对象的抽象数据类型
    Date(int year, int month, int day)  #构造表示year/month/day的对象
    difference(Date d1, Date d2)        #求出d1和d2的日期差
    plus(Date d, int n)                 #计算出日期d之后n天的日期
    num_ date(int year, int n)          #计算year年第n天的日期
    adjust(Date d, int n)               #将日期d调整n天( n为带符号整数)
'''
