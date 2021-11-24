###########################################################
print('function')
###########################################################

print('\n------------------------------------------')

def f():
    print('Golzari')

f()

print('\n------------------------------------------')

def g():
    return 'Golzari'

print(g())

print('\n------------------------------------------')

def h(p):
    print(p)

h('Golzari')

print('\n------------------------------------------')

def f(x, y):
    if x > y:
        return x
    return y

def g(x, y, z):
    return f(x, f(y, z))

print(g(3, 8, 2))  # 8

print('\n------------------------------------------')

x = 7

def func():
    global x
    print(x)  # 7
    x = 3
    print(x)  # 3

func()
print(x)  # 3

print('\n------------------------------------------')

def f(a, b):
    a *= 2
    b += 3
    return a, b

x = 4
y = 6
m, n = f(x, y)
print(m)  # 8
print(n)  # 9

print('\n------------------------------------------')

def f(lst):
    lst[0] *= 2
    lst[1] /= 3

a = [4, 9]
f(a)
print(a[0])  # 8
print(a[1])  # 3.0

print('\n------------------------------------------')

def h(my_dict):
    my_dict['x'] *= 2
    my_dict['y'] /= 3

d = {'x': 4, 'y': 9}
h(d)
print(d['x'])  # 8
print(d['y'])  # 3.0

print('\n------------------------------------------')

def test(x, y):
    print(x, y)

test(5, 2)  # 5 2
test(x=5, y=2)  # 5 2
test(y=2, x=5)  # 5 2
test(5, y=2)  # 5 2

print('\n------------------------------------------')

def harmonic(n, r=1):
    total = 0.0
    for i in range(1, n + 1):
        total += 1.0 / (i ** r)
    return total

print(harmonic(4))
print(harmonic(4, r=2))
print(harmonic(4, r=3))

print('\n------------------------------------------')

# keyword only argument

def f(*, x=8):
    print(x)

f()  # 8
f(x=2)  # 2

# f(3)     #  f() takes 0 positional arguments but 1 was given

print('\n------------------------------------------')

# var arguments

def add_more(a, b, *c):
    print(a + b + sum(c))

add_more(5, 2, 7, 8, 12)  # 5+2+7+8+12=
add_more(2, 6)  # 8

print('\n------------------------------------------')

def f(*x, y='.'):
    return y.join(x)

print(f('ali', 'reza'))  # ali.reza
print(f('ali', 'reza', 'sara', y='/'))  # ali/reza/sara

print('\n------------------------------------------')

def test(a, *, b=7, c=9):
    print(a, b, c)

test(5)  # 5  7  9
test(1, b=4)  # 1  4  9

# test(1, b=2, 6)    #  positional argument follows keyword argument

# test(1, 3, c=4)
'''
test() takes 1 positional argument but 2 positional arguments 
(and 1 keyword-only argument) were given
'''

print('\n------------------------------------------')

def f(a, b, *c, **d):
    print(a)  # 3
    print(b)  # 4
    print(c)  # (7, 1, 6)
    print(d)  # {'x': 5, 'y': 7, 'z': 9}

f(3, 4, 7, 1, 6, x=5, y=7, z=9)

print('\n------------------------------------------')

def count_char(s):
    d = {}
    for i in s:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    return d

print(count_char('abbcfab'))  # {'a': 2, 'b': 3, 'c': 1, 'f': 1}

print('\n------------------------------------------')

'''
switch(a){
   case 1: return 'one' ;break;
   case 2: return 'two' ;break;
   defualt :return 'nothing';
}
'''

print('\n------------------------------------------')

def switch(a):
    d = {1: 'one', 2: 'two'}
    return d.get(a, 'nothing')

print(switch(1))  # one
print(switch(2))  # two
print(switch(3))  # nothing

print('\n------------------------------------------')

a = [1, 2, 3, 1, 4, 2]

def unique_list(lst):
    r = []
    for i in lst:
        if i not in r:
            r.append(i)
    return r

print(unique_list(a))  # [1, 2, 3, 4]

print('\n------------------------------------------')

def unique_list_2(lst):
    return list(set(lst))

print(unique_list_2(a))  # [1, 2, 3, 4]

print('\n------------------------------------------')

print('--- PEP 484 --------')

def greeting(name: str) -> str:
    return 'Hello ' + name

print(greeting('farshid'))  # Hello farshid

print('\n------------------------------------------')

def add(x: int, y: int) -> int:
    '''
     sum two number
    '''
    print(x + y)

add(2, 3)  # 5

print(add.__annotations__)
# {'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}

print(add.__doc__)  # sum two number

###############################################################
print('recursive')
##############################################################

'''
iterative:
            n! = 1*2*3*...*n

recursive:
            n! = n * (n-1)!
            1! = 1

4! = 4 * 3! = 4 * 6 = 24
3! = 3 * 2! = 3 * 2 = 6
2! = 2 * 1! = 2 * 1 = 2
1! = 1

'''

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(4))      #24

print('\n------------------------------------------')

def f(n, base):
    s = '0123456789ABCDEF'
    if n < base:
        return s[n]
    else:
        return f(n // base, base) + s[n % base]

print(f(25, 16))      #19

'''
f(25,16) = f(1,16) + s[9] = 1 + 9 = 19
f(1,16)  = s[1]  = 1
'''

print(f(8,2))         # 1000

print('\n------------------------------------------')

def gcd(p, q):
    if q == 0:
        return p
    return gcd (q, p % q)

print(gcd(12, 36))

'''
gcd(12,36) = gcd(36,12) = 12
gcd(36,12) = gcd(12, 0) = 12
gcd(12, 0) = 12
'''

print('\n------------------------------------------')

def binary_search(lst, x, start=0, end=None):
    if end is None:
        end = len(lst) - 1
    if start > end:
        return False
    mid = (start + end) // 2
    if x == lst[mid]:
        return mid
    if x < lst[mid]:
        return binary_search(lst, x, start, mid - 1)
    return binary_search(lst, x, mid + 1, end)

a = [2, 4, 7, 12, 19, 25, 38]
print(binary_search(a, 19 ))    # 4
print(binary_search(a, 4 ))     # 1
print(binary_search(a, 20))     # False

print('\n------------------------------------------')

#  0 1 1 2 3 5 8 ...

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

# print(fib(60))

print('\n------------------------------------------')

#  0 1 1 2 3 5 8 ...
memo = [0] * 100
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if memo[n]==0:
        memo [n] = fib(n-1) + fib(n-2)
    return memo[n]

print(fib(60))      #1548008755920

print('\n------------------------------------------')

def fib(n):
    F = [0] * (n + 1)
    F[0] , F[1] = 0, 1
    for i in range(2, n+1):
        F[i] = F[i-1] + F[i-2]
    return F[n]

print(fib(60))      #1548008755920

print('\n------------------------------------------')

##############################################################
print('lambda')
##############################################################

add = lambda x, y : x + y
print(add(2,3))       #5

print('\n------------------------------------------')

f = lambda x, y : (x + y, x - y)
print(f(2,3))       #(5, -1)

print('\n-----------------Map-------------------------')
lst = ('maHSa', 'AlI')
print(list(map(str.lower, lst)))        #['mahsa', 'ali']

print('\n------------------------------------------')

a = ['maHSa', 'AlI']
b = [20, 35]

print(list(zip(a, b)))                          #[('maHSa', 20), ('AlI', 35)]
#or
print(list(map(lambda x, y : (x, y), a, b)))    #[('maHSa', 20), ('AlI', 35)]

print('\n------------------------------------------')

a = [1, 2]
b = [3, 4]

print(list(map(lambda x,y : x+y , a, b)))           #[4, 6]

print('\n------------------------------------------')

a = [16, 7, 14, 6]
print(list(map(lambda x : x < 10, a)))              #[False, True, False, True]

print('\n-------------------Filter-----------------------')

a = [16, 7, 14, 6]
print(list(filter(lambda x : x < 10, a)))           #[7, 6]

print('\n------------------------------------------')

a = [16, 7, '', 14, 6, '']
print(list(filter(None, a)))           #[16, 7, 14, 6]

print('\n-------------------Reduce-----------------------')

from functools import reduce

lis = [16, 7, 14, 6]
add = lambda a, b : a+b

print(reduce(add, lis))     #43 (((16, 7)+14)+6)

print('\n-------------------sorted-----------------------')
lst = [16, 7, 14, 6]
print(sorted(lst))         #[6, 7, 14, 16]

print('\n------------------------------------------')

d = {'Ali': 12, 'Taha': 2, 'Mahsa': 15}
print(sorted(lst))         #[6, 7, 14, 16]
print(sorted(d.items(), key = lambda x: x[0]))  #[('Ali', 12), ('Mahsa', 15), ('Taha', 2)]


#  دانشگاه شهید مدنی آذربایجان
#  برنامه نویسی مقدماتی با پایتون
#  امین گلزاری اسکوئی
# https://github.com/Amin-Golzari-Oskouei/Python-Programming-Course-Basic-2021
# https://drive.google.com/drive/folders/1ZsQjBJJ4UAAp9zrGxm3c4qrhnvGBUYHw
