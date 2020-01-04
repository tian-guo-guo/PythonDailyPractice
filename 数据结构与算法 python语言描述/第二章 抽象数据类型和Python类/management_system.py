'''
为一个学校的人员管理系统定义所需的表示人员信息的类。

分析：
学校里有两大类人员，即学生和教职工，他们都是需要在系统里表示的对象。分析这两类
人员需要记录的信息，可以看到这里有一些值得注意的情况:与两类人员有关的信息中存在一
些公共部分，又有各自的特殊情况: 
●首先，作为人员信息，无论学生或教职工都有姓名、性别、年龄等公共信息。另外，
为了便于学校管理，学生应该有一-个学号， 教职工也应该有一个职工号。
●作为学生应该有学习记录，包括属于哪个院系、注册时间，特别是学习期间已经学过
的各门课程及其成绩等。
●教职工应该有人职时间、院系、职位和工资等信息。
由于两类人员的信息既有共性又有特殊性，特别适合采用面向对象的类继承机制处理。这里的
考虑是首先定义一一个公共的人员类，提供记录和查询人员基本信息的功能。然后从这个公共类
分别派生出表示学生的类和表示教职工的类。

基本人员ADT的设计：
ADT Person：                        #定义人员抽象数据类型
    Person(self, strname, strsex, tuple birthday, str ident) # 构造人员对象
    id(self)                        #取得该人员记录中的人员编号
    name(self)                      #取得该人员记录中的姓名
    sex(self)                       #取得该人员记录中的性别
    birthday(sel)                   #取得该人员记录中的出生年月日
    age(self)                       #取得该人员的年龄
    set_ name(self, str name)       #修改人员姓名
    <(self, Person another)         #基于人员编号比较两个记录
    details(self)                   #给出人员记录里保存的数据详情

学生ADT的设计：
ADT Student(Person):                #定义学生ADT
    Student(self, strname, strsex, tuple birthday, str department) # 构造学生对象
    department(self)                #取得学生所属院系
    en_year(self)                  #取得学生入学年度
    scores(self)                    #取得学生的成绩单
    set_course(self, str course_ name)#设置选课
    set_score(self, str course_ name, int score)#设置课程成绩

教职工ADT的设计：
ADT Staff(Person):                  #定义教职工ADT
    Staff(self, strname, strsex, tuple birthday, tuple entry_ date) # 构造教职工对象
    department(self)                #取得教职工的所属院系
    salary(self)                    #取得教职工的工资额
    entry_ date(self)               #取得教职工的人职时间
    position(self)                  #取得教职工的职位
    set_ salary(self, int amount)   #设置工资额
'''

# 先定义两个异常类，以便在定义人事类的操作中遇到异常情况时引发特殊的异常
# 人们在定义自己的特殊异常类时，多数选择一个合适的Python标准异常作为基类，
# 派生时不定义任何方法或数据属性

import datetime

class PersonTypeError(TypeError):
    pass

class PersonValueError(ValueError):
    pass 

# 公共人员类的实现
class Person: 
    _num = 0 

    def __init__(self, name, sex, birthday, ident):
        '''检查参数的合法性，并加入实例计数功能'''
        if not (isinstance(name, str) and sex in ('女', '男')):
            raise PersonValueError(name, sex)
        try:
            birth = datetime.date(*birthday)    # 生成一个日期对象
        except:
            raise PersonValueError('Wrong date: ', birthday)
        self._name = name 
        self._sex = sex 
        self._birthday = birth 
        self._id = ident 
        Person._num += 1    # 实例计数
    
    def id(self):
        return self._id 
    def name(self):
        return self._name
    def sex(self):
        return self._sex 
    def birthday(self):
        return self._birthday
    def age(self):
        return (datetime.date.today().year - self._birthday.year)
    def set_name(self, name):   # 修改名字
        if not isinstance(name, str):
            raise PersonValueError('set_name', name)
        self._name = name 
    def __lt__(self, another):
        if not isinstance(another, Person):
            raise PersonTypeError(another)
        return self._id < another._id 

    @classmethod 
    def num(cls):
        return Person._num 
    def __str__(self):
        return ' '.join((self._id, self._name, self._sex, str(self._birthday)))
    def details(self):
        return ', '.join(('编号：'+self._id,
                          '姓名：'+self._name,
                          '性别：'+self._sex,
                          '出生日期：'+str(self._birthday)))

p1 = Person('谢雨洁', '女', (1995, 7, 30), '1201510111')
p2 = Person('汪力强', '男', (1990, 2, 17), '1201380324')
p3 = Person('张子玉', '女', (1974, 10, 16), '0197401032')
p4 = Person('李国栋', '男', (1962, 5, 24), '0196212018')

plist2 = [p1, p2, p3, p4]
for p in plist2:
    # 由于定义了__str__方法，因此可以直接用print输出Person对象
    print(p)

print('\nAfter sorting:')
plist2.sort()
for p in plist2:
    print(p.details())
print('People created:', Person.num(), '\n')

print('-'*80)

# 学生类的实现
'''
需要关注几件事:
①Student对象也是Person对象，因此，在建立Student对象时，应该调用Person类的
初始化函数，建立起表示Person对象的那些数据属性。
②这里希望Student类实现一种学号生成方式。为了保证学号的唯一性， 最简单的技术就是
用一个计数变量，每次生成学号时将其加一。这个变量应该是Student类内部的数据，
但又不属于任何Student实例对象，因此应该用类的数据属性表示。
③学号生成函数只在student类的内部使用，但并不依赖于Student的具体实例。根据这些
情况，该函数似乎应该定义为静态方法。但是，这个函数并不是独立的，它依赖于Student
类中的数据属性。根据前面的讨论，应该将其定义为类方法，在其中实现所需的学号生成规则。
'''
class Student(Person):
    _id_num = 0 

    @classmethod 
    def _id_gen(cls):       # 实现学号生成规则
        cls._id_num += 1 
        year = datetime.date.today().year 
        return '1{:04}{:05}'.format(year, cls._id_num)

    def __init__(self, name, sex, birthday, department):
        Person.__init__(self, name, sex, birthday, Student._id_gen())
        self._department = department
        self._enroll_date = datetime.date.today() 
        self._courses = {}      # 一个空字典

    def set_course(self, course_name):
        self._courses[course_name] = None 
    
    def set_score(self, course_name, score):
        if course_name not in self._courses:
            raise PersonValueError('No this course seleted:', course_name)
        self._courses[course_name] = score 
    
    def scores(self):
        return [(cname, self._courses[cname]) for cname in self._courses]

    # 重写details方法，因为Student对象包含更多的信息
    def details(self):
        return ', '.join((Person.details(self), 
                          '入学日期：' + str(self._enroll_date),
                          '院系：' + self._department,
                          '课程记录：' + str(self.scores())))


s1 = Student('谢雨洁', '女', (1995, 7, 30), '计算机软件')
s2 = Student('汪力强', '男', (1990, 2, 17), '通信')
s3 = Student('张子玉', '女', (1974, 10, 16), '数学')
s4 = Student('李国栋', '男', (1962, 5, 24), '化学')

slist2 = [s1, s2, s3, s4]
for s in slist2:
    # 由于定义了__str__方法，因此可以直接用print输出Person对象
    print(s)

print('\nAfter sorting:')
slist2.sort()
for s in slist2:
    print(s.details())
print('Student created:', Student.num(), '\n')

print('-'*80)

# 教职工类的实现
'''
staff类也需要为教职工对象实现一个职工号生成函数，同样定义为类方法，基于staff类
的数据属性完成工作。这里假定职工号的首字符为0，其中编码了具体教职工的出生年份，
在加上一个内定的序号。
'''
class Staff(Person):
    _id_num = 0 

    @classmethod
    def _id_gen(cls, birthday):         # 实现职工号生成规则
        cls._id_num += 1 
        birth_year = datetime.date(*birthday).year 
        return '0{:04}{:05}'.format(birth_year, cls._id_num)

    def __init__(self, name, sex, birthday, entry_date=None):
        super().__init__(name, sex, birthday, Staff._id_gen(birthday))
        if entry_date:
            try:
                self._entry_date = datetime.date(*entry_date)
            except:
                raise PersonValueError('Wrong_date:', entry_date)
        else:
            self._entry_date = datetime.date.today()
            self._salary = 1720     # 默认设为最低工资，可修改
            self._departmet = '未定' # 需要另行设定
            self._position = '未定'  # 需要另行设定
        
    def set_salary(self, amount):
        if not type(amount) is int:
            raise TypeError 
        self._salary = amount 

    def set_position(self, position):
        self._position = position 

    def set_department(self, department):
        self._departmet = department

    def details(self):
        return ', '.join((super().details(),
                          '入职日期：' + str(self._entry_date),
                          '院系：' + self._departmet,
                          '职位：' + self._position, 
                          '工资：' + str(self._salary)))

p1 = Staff('张子玉', '女', (1974, 10, 16))
p2 = Staff('李国栋', '男', (1962, 5, 24))
print(p1)
print(p2)
p1.set_department('数学')
p1.set_position('副教授')
p1.set_salary(8400)
print(p1.details())
print(p2.details())