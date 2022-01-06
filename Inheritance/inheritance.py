# inheritance

class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print('name: ', self.name)


class Student(Person):
    def __init__(self, name, score):
        # Person.__init__(self, name)
        super().__init__(name)
        self.score = score

    def welcome(self):
        print('welcome ', self.name)

stu = Student('Amin', 19)
stu.welcome()   #welcome  Amin
stu.show()      #name:  Amin

print('\n---------------------------------------')
#parent class
class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(self.name)

#child class
class Emplyee(Person):
    def __init__(self, name, id, salary, post):
        Person.__init__(self, name, id)
        self.salary = salary
        self.post = post

emp1 = Emplyee('Ali', 123456, 8000000, 'Boss')
emp2 = Emplyee('sara', 789456, 4000000, 'secreter')

emp1.display()   #Ali
emp2.display()   #Sara

print('\n---------------------------------------')

class Rect:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def mohit(self):
        return (2 * self.x) + (2 * self.y)

class Square(Rect):
    def __init__(self, z):
        Rect.__init__(self, x = z, y = z)
        super().__init__(x = z, y = z)


r = Rect(2, 3)
print(r.area())     #6
print(r.mohit())    #10

s = Square(2)
print(s.area())     #4
print(s.mohit())    #8

print('\n----------------__mro__: Methods Resolution Order-----------------------')

print(Square.__mro__)   #(<class '__main__.Square'>, <class '__main__.Rect'>, <class 'object'>)
print(Rect.__mro__)     #(<class '__main__.Rect'>, <class 'object'>)

print('\n----------------Multiple Inheritance-----------------------')

class B1:
    def __init__(self, x):
        self.x = x
        print(x)

class B2:
    def __init__(self, y):
        self.y = y
        print(y)

class D(B1, B2):
    def __init__(self, z):
        self.z = z
        print(z)
        B1.__init__(self, 2)
        B2.__init__(self, 3)

d = D(1)   #1   2   3

print(D.__mro__)   #(<class '__main__.D'>, <class '__main__.B1'>, <class '__main__.B2'>, <class 'object'>)

print('or')


class B1:
    def __init__(self, x):
        self.x = x
        print(x)

class B2:
    def __init__(self, y):
        self.y = y
        print(y)

class D(B2, B1):
    def __init__(self, z):
        self.z = z
        print(z)
        B2.__init__(self, 3)
        B1.__init__(self, 2)


d = D(1)   #1   3   2

print(D.__mro__) #(<class '__main__.D'>, <class '__main__.B2'>, <class '__main__.B1'>, <class 'object'>)

print('\n---------------------------------------')

class Square:
    def __init__(self, x):
        self.x = x

    def area(self):
        return self.x * self.x

    def peimeter(self):
        return 4 * self.x

class Triangle:
    def __init__(self, y, z):
        self.y = y
        self.z = z

    def area(self):
        return 0.5 * self.y * self.z

class Pyramid(Square, Triangle):
    def __init__(self, b, s):
        self.s = s
        Square.__init__(self, x = b)
        Triangle.__init__(self, y = b, z = s)

    def area(self):
        a = Square.area(self)
        p = Square.peimeter(self)
        return a + 0.5 * p * self.s

t = Triangle(3, 6)
print(t.area())   #9.0 (0.5 * 3 * 6)

p = Pyramid(2, 5)
print(p.area())   #24.0  ((2*2) + 0.5 * 4*2 * 5)

print('\n----------------Multilevel Inheritance-----------------------')

class A:
    def __init__(self, name):
        self.name = name

    def getname(self):
        return self.name

class B(A):
    def __init__(self, name, age):
        self.age = age
        A.__init__(self, name)

    def getage(self):
        return self.age

class C(B):

    def __init__(self, name, age, score):
        self.score = score
        B.__init__(self, name, age)

    def getscore(self):
        return self.score

ob = C('Amin', 27, 19)
print(ob.name)        #Amin
print(ob.getname())   #Amin
print(ob.getscore())  #19
print(ob.getage())    #27

print('\n---------------------------------------')

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class HE(Employee):
    def __init__(self, name , id, hw, hr):
        self.hw = hw
        self.hr = hr
        super().__init__(name, id)

    def h(self):
        return self.hw * self.hr

class SE(Employee):
    def __init__(self, name , id, s):
        self.s = s
        super().__init__(name, id)

    def h(self):
        return self.s

class CE(SE):
    def __init__(self, name , id, s, c):
        self.c = c
        super().__init__(name, id, s)

    def h(self):
        return self.s + self.c

class P:
    def payroll(self, lst):
        for i in lst:
            print(f'{i.id}: {i.name} = {i.h()}')

ob1 = HE('Sara', 1, 4, 100000)
ob2 = SE('Ali', 2, 8000000)
ob3 = CE('Mahsa', 3, 5000000, 3000000)

ob = P()
ob.payroll([ob1, ob2, ob3])

print('\n-----------------Dimaond problem----------------------')

class A:
    def f(self):
        print('A')

class B(A):
    def f(self):
        print('B')

class C(A):
    def f(self):
        print('C')

class D(B, C):
        pass

d = D()
d.f()  #B

print('or')

class A:
    def f(self):
        print('A')

class B(A):
    def f(self):
        print('B')

class C(A):
    def f(self):
        print('C')

class D(C, B):
        pass

d = D()
d.f()  #C

print('\n---------------------------------------')

class B:
    def __init__(self, x, y):
        self._a = x          #Ptotected
        self.__b = y         #Private

    def f(self):
        print(self._a)
        print(self.__b)

class D(B):
    def h(self):
        print(self._a)
        # print(self.__b)  #Error

d = D(1, 2)
d.h()  #1
d.f()  #1   2

print('\n---------------------------------------')

class B:
    def __f(self):
        return 'A'

    def g(self):
        print(self.__f())

class D(B):
    def __f(self):
        return 'B'

d = D()
d.g()  #A

print('\n---------------------------------------')

class B:
    def _f(self):
        return 'A'

    def g(self):
        print(self._f())

class D(B):
    def _f(self):
        return 'B'

d = D()
d.g()  #B

#  دانشگاه شهید مدنی آذربایجان
#  برنامه نویسی مقدماتی با پایتون
#  امین گلزاری اسکوئی
# https://github.com/Amin-Golzari-Oskouei/Python-Programming-Course-Basic-2021
# https://drive.google.com/drive/folders/1ZsQjBJJ4UAAp9zrGxm3c4qrhnvGBUYHw
















