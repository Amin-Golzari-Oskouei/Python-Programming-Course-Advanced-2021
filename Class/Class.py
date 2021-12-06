'''
   OOP :
       class
       object
       __init__

'''

class Test:
    ''' class for add  , mul '''
    def set_var (self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

ob1 = Test()
ob1.set_var(1, 2)

print(ob1.a)    #1
print(ob1.b)    #2

print(ob1.add())   #3
print(ob1.mul())   #2

print(ob1.__doc__)    #class for add  , mul
print(ob1.__dict__)   #{'a': 1, 'b': 2}

ob2 = Test()
ob2.set_var(3, 4)

print(ob2.a)    #3
print(ob2.b)    #4

print(ob2.add())   #7
print(ob2.mul())   #12

print(ob2.__doc__)    #class for add  , mul
print(ob2.__dict__)   #{'a': 3, 'b': 4}

del ob1
# print(ob1.a)    #NameError: name 'ob1' is not defined

del ob2.a
print(ob2.__dict__)   #{'b': 4}

print('\n-------------------init---------------------')

class Test:
    ''' class for add  , mul '''
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

ob1 = Test(1, 2)

print(ob1.a)    #1
print(ob1.b)    #2

print(ob1.add())   #3
print(ob1.mul())   #2

print(ob1.__doc__)    #class for add  , mul
print(ob1.__dict__)   #{'a': 1, 'b': 2}

ob2 = Test(3, 4)

print(ob2.a)    #3
print(ob2.b)    #4

print(ob2.add())   #7
print(ob2.mul())   #12

print(ob2.__doc__)    #class for add  , mul
print(ob2.__dict__)   #{'a': 3, 'b': 4}

print('\n----------------------------------------')

class Book:
    def __init__(self,author ,title):
        self.author = author
        self.title = title

    def Info(self):
        print(self.title + ': ' + self.author)

x = Book('Golzari', 'Deep Learning with Python')
x.Info()         #Deep Learning with Python: Golzari

y = Book('Hashemzadeh', 'Machine Learning')
y.Info()         #Machine Learning: Hashemzadeh

print('\n----------------------------------------')

class Students:
    def __init__(self, name, score = None):
        self.d = {}
        self.d['name'] = name
        self.d['score'] = score

    def get_stu(self):
        return self.d

lst = []

ob1 = Students('Mahsa', 15)
ob2 = Students('ali', 18)

lst.append(ob1.get_stu())
lst.append(ob2.get_stu())

print(lst)             #[{'name': 'Mahsa', 'score': 15}, {'name': 'ali', 'score': 18}]
print(lst[0])          #{'name': 'Mahsa', 'score': 15}

print('\n----------------------------------------')

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r ** 2 * 3.14

x = Circle(2)
print(x.area())     #12.56
print(isinstance(x, Circle))      #True
print(isinstance(y, Circle))      #False

print('\n----------------------------------------')

d = dict()
print(type(d))    #<class 'dict'>

a = 1
print(type(a))    #<class 'int'>

print('\n----------------------------------------')

class Counter:
    def __init__(self, x):
        self.x = x

    def Up(self):
        self.x += 1

    def Down(self):
        self.x -= 1

ob = Counter(4)
print(ob.x)       #4
ob.Up()
ob.Up()
print(ob.x)       #6
ob.Down()
print(ob.x)       #5

print('\n----------------------------------------')

class C():
    def __init__(self):
        self.s = ''

    def get_string(self):
        self.s = input('input: ')

    def show(self):
        print(self.s.upper())

# ob = C()
# ob.get_string()
# ob.show()

print('\n----------------------------------------')

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i


x = Complex(2, 4)
print(x.r)    #2
print(x.i)    #4

print('\n----------------------------------------')

class Email:

    def f(self):
        self.send = False

    def g(self):
        self.send = True

ob = Email()
ob.f()
print(ob.send)   #False
ob.g()
print(ob.send)   #True

print('\n----------------------------------------')

class Machine:

    Model = 'peugeot'

    def __init__(self, t):
        self.t = t

m1 = Machine('206')
m2 = Machine('207')

print(m1.Model)   #peugeot
print(m2.Model)   #peugeot

print(m1.t)   #206
print(m2.t)   #207

print('\n----------------------------------------')

class C:
    lst = []

    def __init__(self, name):
        self.name = name

    def f(self, x):
        self.lst.append(x)

ob1 = C('A')
ob2 = C('B')

ob1.f(1)
ob1.f(2)
ob1.f(3)

print(ob1.lst)   #[1, 2, 3]
print(ob2.lst)   #[1, 2, 3]

ob2.f(4)

print(ob1.lst)   #[1, 2, 3, 4]
print(ob2.lst)   #[1, 2, 3, 4]

print('\n----------------------------------------')

class C:

    def __init__(self, name):
        self.name = name
        self.lst = []

    def f(self, x):
        self.lst.append(x)

ob1 = C('A')
ob2 = C('B')

ob1.f(1)
ob1.f(2)
ob1.f(3)

print(ob1.lst)   #[1, 2, 3]
print(ob2.lst)   #[]

ob2.f(4)

print(ob1.lst)   #[1, 2, 3]
print(ob2.lst)   #[4]

print('\n----------------------------------------')

class Students:

    stream = 'CSE' #class var

    def __init__(self, name, score):
        self.name = name       #instance var
        self.score = score     #instance var

# objects of students class
s1 = Students('Ali', 18)
s2 = Students('Mahsa', 15)

print(s1.name)            #Ali
print(s2.name)            #Mahsa

print(s1.stream)           #CSE
print(s2.stream)           #CSE

print(Students.stream)     #CSE
# print(Students.name)       #AttributeError

print('\n----------------------------------------')

class Dog:
    animal = 'dog'

    def __init__(self, a, c):
        self.a = a
        self.c = c

d1 = Dog('pug', 'brown')
d2 = Dog('bulldog', 'black')

print(d1.animal)   #dog
print(d2.animal)   #dog

print(d1.c)   #brown
print(d2.c)   #black

print('\n------------------Private----------------------')

class Test:
    def __init__(self, a, b):
        self.a = a          #Public
        self.__b = b        #private

    def f(self):
        self.__b += 1
        print(self.__b)

ob = Test(1, 2)
print(ob.a)        #1
# print(ob.__b)    #AttributeError

ob.f()             #3

print(ob.__dict__)    #{'a': 1, '_Test__b': 3}
print(ob._Test__b)    #3

ob._Test__b = 8
print(ob._Test__b)    #8

print('\n----------------------------------------')

class S:
    def __init__(self, x):
        self.__a = x

    def f(self):
        print(self.__a, end =' ')
        self.__a +=1
        return (self.__a)

    def g(self, m):
        print(m + self.f())

ob = S(1)
print(ob.__dict__)    #{'_S__a': 1}
print(ob.f())         #1 2
ob.g(5)               #2 8

print('\n----------------------------------------')

class AB:
    __x = 3

    def show(self):
        print(self.__x)

ob = AB()
ob.show()         #3
print(ob._AB__x)  #3

print('\n-----------------Private Method-----------------------')

class ABC:
    def __f(self):
        print(1)

    def g(self):
        return (self.__f())

ob = ABC()
ob.g()          #1
# ob.__f()      #AttributeError
ob._ABC__f()    #1





















































































