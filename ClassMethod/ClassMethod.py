#decorator

def d(func):
    def wrapper():
        print('before')
        func()
        print('after')
    return wrapper

def f():
    print('Hello')

x = d(f)
x()

# before
# Hello
# after

print('\n---------------------------------')

def d(func):
    def wrapper():
        print('before')
        func()
        print('after')
    return wrapper

@d
def f():
    print('Hello')

f()

# before
# Hello
# after

print('\n---------------------------------')

def d(func):
    def wrapper():
        print('before')
        func()
        func()
        print('after')
    return wrapper


@d
def f():
    print('Hello')

f()

# before
# Hello
# Hello
# after

print('\n---------------------------------')

def d(func):
    def w(a):
        func(a + 3)
    return w

@d
def g(x):
    print(x)

g(5)  #8

print('\n---------------------------------')

'''
instance method:
      def f(self, a):
          pass

class method:
      @classmethod
      def g(cls, a):
         pass

static method:
      @staticmethod
      def h(a):
          pass
'''

class C:
    def __init__(self, a):
        self.a = a

    def f(self, i):
        print(self.a)
        print(i + 3)

ob = C(1)
print(ob.a)       #1
ob.f(3)           #1    6

# print(C.a)  #AttributeError: type object 'C' has no attribute 'a'
# print(C.f(3)) #TypeErro

print('\n---------------------------------')

class A:
    def __init__(self, x):
        self.x = x

    @staticmethod
    def func_sum(m, n):
        print(m + n)
        # print(self.x)

A.func_sum(2, 3)   #5

ob = A(8)
ob.func_sum(2, 4)  #5

print(A.func_sum == ob.func_sum)  #True

print('\n---------------------------------')

class D:
    def __init__(self, x):
        self.x = x

    @classmethod
    def h(cls, t):
        print(t + 2)
        return cls(t)

ob = D(0)
ob.h(2)   #4
D.h(2)    #4

print(D.h == ob.h)    #True
print(ob.h(15).x)     #17   15

print('\n---------------------------------')

from datetime import date

class C:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def f(cls, name, year):
        y = date.today().year - year
        return cls(name, y)

    @staticmethod
    def s(age):
        return age <= 30

ob = C.f('Amin', 1994)
print(ob.age)    #28
print(ob.name)   #Amin

print(ob.s(28))  #True

print('\n---------------------------------')

class Date:
    def __init__(self, day = 0, month = 0, year = 0):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def f(cls, d):
        day, month, year = map(int, d.split('-'))
        return cls(day, month, year)

    @staticmethod
    def g(d):
        day, month, year = map(int, d.split('-'))
        return day <= 31 and month <= 12

d = Date.f('05-01-2022')
print(d.year)      #2022
print(d.month)     #01
print(d.day)       #5

print(Date.g('05-01-2022'))   #True
print(Date.g('05-20-2022'))   #False

print('\n---------------------------------')

class Person:
    def __init__(self, name , family):
        self.name = name
        self.family = family

    @property
    def f(self):
        return '%s %s' %(self.name, self.family)

    @f.setter
    def f(self, s):
        name, family = s.split(' ')
        self.name = name
        self.family = family

ob = Person('sara', 'rasti')
print(ob.f)

ob.f = 'amin golzari'
print(ob.name)     #amin
print(ob.family)   #golzari

print('\n---------------------------------')

class Test:
    def f(k):
        return k.__name__
    f = classmethod(f)

print(Test.f())  #Test

print('\n---------------------------------')

class Nmubers:
    a = 3
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    @classmethod
    def mul(cls, b):
        return cls.a * b

    @staticmethod
    def sub(b, c):
        return b - c

    @property
    def value(self):
        return (self.x, self.y)

    @value.setter
    def value(self, t):
        self.x, self.y = t

    @value.deleter
    def value(self):
        del self.x
        del self.y

ob = Nmubers(2, 3)
print(ob.add())       #5
print(ob.mul(4))      #12
print(ob.sub(2, 3))   #-1

print(ob.value)       #(2, 3)
ob.value = (6, 8)
print(ob.value)       #(6, 8)

print('\n---------------------------------')

def d(func):
    def w():
        '''hello'''
        print(func.__name__)
        return func()
    return w

@d
def f(x):
    '''python'''
    return x + 2

print(f.__name__)   #w
print(f.__doc__)    #hello

print('\n---------------------------------')

from functools import wraps

def d(func):
    @wraps(func)
    def w():
        '''hello'''
        print(func.__name__)
        return func()
    return w

@d
def f(x):
    '''python'''
    return x + 2

print(f.__name__)   #f
print(f.__doc__)    #python

print('\n---------------------------------')

class B:
    def __init__(self, a):
        self.a = a

    def f(self):
        return self.a + 2

class D(B):
    pass

ob = D(3)
print(ob.f())   #5

print('\n---------------------------------')

from abc import ABC, abstractmethod

class B(ABC):
    def __init__(self, a):
        self.a = a
        super().__init__()

    @abstractmethod
    def f(self):
        pass

class D(B):
    def f(self):
        return self.a + 2

class E(B):
    def f(self):
        return self.a + 3

ob = D(3)
print(ob.f())   #5

ob2 = E(3)
print(ob2.f())   #6

#  دانشگاه شهید مدنی آذربایجان
#  برنامه نویسی مقدماتی با پایتون
#  امین گلزاری اسکوئی
# https://github.com/Amin-Golzari-Oskouei/Python-Programming-Course-Basic-2021
# https://drive.google.com/drive/folders/1ZsQjBJJ4UAAp9zrGxm3c4qrhnvGBUYHw










