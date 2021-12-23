'''
dunder : double underscore

__init__
__str__
__len__
__getitem__
__setitem__
__repr__
__call__

__add__
__gt__
__lt__
__eq__

'''

class A:
    def __init__(self):
        self.lst = [45, 89, 12]

ob = A()
print(ob)     #<__main__.A object at 0x0000021F8C66E220>

print('\n-------------------------------------')

class A:
    def __init__(self):
        self.lst = [45, 89, 12]

    def __str__(self):
        return str(self.lst)

ob = A()
print(ob)     #[45, 89, 12]

print('\n-------------------------------------')

class A:
    def __init__(self):
        self.lst = [45, 89, 12]

    def __str__(self):
        return str(self.lst)

ob = A()
# print(len(ob))     #TypeError: object of type 'A' has no len()


class A:
    def __init__(self):
        self.lst = [45, 89, 12]

    def __str__(self):
        return str(self.lst)

    def __len__(self):
        return len(self.lst)

ob = A()
print(len(ob))     #3

print('\n-------------------------------------')

class A:
    def __init__(self):
        self.lst = [45, 89, 12]

    def __str__(self):
        return str(self.lst)

    def __len__(self):
        return len(self.lst)

ob = A()
# print(ob[1])     #TypeError: 'A' object is not subscriptable

class A:
    def __init__(self):
        self.lst = [45, 89, 12]

    def __str__(self):
        return str(self.lst)

    def __len__(self):
        return len(self.lst)

    def __getitem__(self, i):
        return self.lst[i]

ob = A()
print(ob[1])     #89

print('\n-------------------------------------')

class A:
    def __init__(self):
        self.lst = [45, 89, 12]

    def __str__(self):
        return str(self.lst)

    def __len__(self):
        return len(self.lst)

    def __getitem__(self, i):
        return self.lst[i]

ob = A()
# ob[1] = 90   #TypeError: 'A' object does not support item assignment


class A:
    def __init__(self):
        self.lst = [45, 89, 12]

    def __str__(self):
        return str(self.lst)

    def __len__(self):
        return len(self.lst)

    def __getitem__(self, i):
        return self.lst[i]
    def __setitem__(self, i, v):
        self.lst[i] = v

ob = A()
ob[1] = 90
print(ob)      #[45, 90, 12]

print('\n-------------------------------------')

class Clock:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def __str__(self):
        return '{0:02d}:{1:02d}:{2:02d}'.format(self.h, self.m,self.s)

ob = Clock(11, 31, 25)
print(ob)    #11:31:25

print('\n-------------------------------------')

class Address:
    def __init__(self, city, street, zipcode):
        self.city = city
        self.street = street
        self.zipcode = zipcode

    def __str__(self):
        lst = []
        lst.append(f'{self.city} - {self.street} - {self.zipcode}')
        return ' '.join(lst)

ob = Address('Tabriz', '17Shahrivar', '123456789')
print(ob)    #Tabriz - 17Shahrivar - 123456789

print('\n-------------------------------------')

class Robot:
    def __init__(self, n, y):
        self.name = n
        self.build_year = y

    def __str__(self):
        return 'name: ' + self.name + ' ,build year: ' + str(self.build_year)

    def __repr__(self):
        return "Robot(\"" + self.name + "\", " + str(self.build_year) + ")"

ob = Robot('RR', 1980)
print(ob)         #name: RR ,build year: 1980
print(repr(ob))   #Robot("RR", 1980)

print('\n---------------__call__----------------------')

class C:
    def __init__(self, size, x, y):
        self.size = size
        self.x = x
        self.y = y

ob = C(300, 10, 20)
print(ob.size) #300
print(ob.x)   #10
print(ob.y)   #20

# ob(30, 50)     #TypeError: 'C' object is not callable

class C:
    def __init__(self, size, x, y):
        self.size = size
        self.x = x
        self.y = y

    def __call__(self, x, y):
        self.x = x
        self.y =y

ob = C(300, 10, 20)
print(ob.size) #300
print(ob.x)   #10
print(ob.y)   #20

ob(30, 50)
print(ob.size) #300
print(ob.x)   #30
print(ob.y)   #50

print('\n-------------------------------------')

#__add__

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        x = self.a + other.a
        y = self.b + other.b
        return x, y

ob1 = Complex(1, 3)    # 1 + 3i
ob2 = Complex(2, 4)    # 2 + 4i
ob3 = ob1 + ob2
print(ob3)             #(3, 7)

print('\n-------------------------------------')

class Test:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a


ob1 = Test('Ali')
ob2 = Test('Reza')
ob3 = ob1 + ob2
print(ob3)  #AliReza

print('\n-------------------------------------')

class AB:
    def __init__(self, a):
        self.a = a

ob1 = AB(1)
ob2 = AB(2)
# print(ob1 > ob2)   #TypeError: '>' not supported between instances of 'AB' and 'AB'

class AB:
    def __init__(self, a):
        self.a = a

    def __gt__(self, other):
        if (self.a > other.a):
            return True
        else:
            return False

ob1 = AB(1)
ob2 = AB(2)
print(ob1 > ob2)   #False

print('\n-------------------------------------')

class AB:
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        if (self.a > other.a):
            return False
        else:
            return True

    def __eq__(self, other):
        if (self.a == other.a):
            return True
        else:
            return False

ob1 = AB(1)
ob2 = AB(2)
print(ob1 < ob2)    #True
print(ob1 == ob2)   #False

print('\n-------------------------------------')

class A:
    def __init__(self , a = None):
        print('init')
        self.__set__(self, a)

    def __set__(self, i, v):
        print('set')
        self.v = v
        print(self.v)

    def __get__(self, i, o):
        print('get')
        return self.v + 1

class B:
    x = A(5)

ob = B()
# init
# set
# 5
ob.x = 8
# set
# 8
print(ob.x)
# get
# 9


#  دانشگاه شهید مدنی آذربایجان
#  برنامه نویسی مقدماتی با پایتون
#  امین گلزاری اسکوئی
# https://github.com/Amin-Golzari-Oskouei/Python-Programming-Course-Basic-2021
# https://drive.google.com/drive/folders/1ZsQjBJJ4UAAp9zrGxm3c4qrhnvGBUYHw








