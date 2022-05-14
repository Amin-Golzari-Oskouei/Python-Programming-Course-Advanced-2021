#pip install numpy

import numpy as np

arr1 = np.arange(100)
print(arr1)

print('--------------------------------')

arr2 = arr1 * 2
print(arr2)

print('--------------------------------')

lst1 = list(range(100))
print(lst1)

print('--------------------------------')
lst2 = [i * 2 for i in lst1]
print(lst2)

print('--------------------------------')

x = np.array([[1, 2], [3,4]])
print(x)
print(x.ndim)
print(x.shape)
print(x.dtype)
print(x * 3)
print(x + 3)
print(x / 3)
print(x ** 3)

print('--------------------------------')

x = np.array([[1, 2], [3,4]])
y = np.array([[-2, 6], [8,3]])

print(x < y)

print('--------------------------------')

lst = [2, 4.5, 6]
print(type(lst))

arr = np.array(lst)
print(arr.dtype)

print('--------------------------------')

arr = np.zeros(3)
print(arr)

arr = np.zeros((3, 3))
print(arr)

arr = np.full(3, 2)
print(arr)

arr = np.full((3,3), 2)
print(arr)

arr = np.identity(3)
print(arr)

print('--------------------------------')

lst = [1, 2]
arr = np.array(lst, dtype = np.int32)
print(arr.dtype)
print(arr)

lst = [1, 2]
arr = np.array(lst, dtype = np.float64)
print(arr.dtype)
print(arr)

print('--------------------------------')
lst = [1, 2]
arr = np.array(lst)
print(arr.dtype)

y = arr.astype(np.float64)
print(y.dtype)

print('---------------Indexing and slicing-----------------')
arr = np.arange(10)
print(arr)
print(arr[3])
print(arr[2:5])

arr[2:5] = 13
print(arr)

x = arr[2:6]
print(x)

arr[:] = 64
print(arr)

print('--------------------------------')

arr = np.arange(8)
print(arr)

print(arr[2:6].copy())

print('---------------arr2d-----------------')

a = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print(a)

print(a[2])
print(a[0])
print(a[0][2])
print(a[2][2])
print(a[2, 2])
print(a.ndim)

print('--------------------------------')

a = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print(a)

print(a.ndim)
print(a.shape)

print(a[:2])
print(a[:1])
print(a[:])
print(a[:2, 1:])
a[:2, 1:] = 0
print(a)

print('--------------------------------')

a = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print(a)

print(a[:2, 0])
print(a[:1, 1])
print(a[:, :1])
print(a[:, :2])

print('---------------arr3d-----------------')

a = np.array([[[1, 2, 3],[4, 5, 6]],[[7, 8, 9], [10, 11, 12]]])
print(a)

print(a.ndim)
print(a.shape)

print(a[0])
print(a[1])

print(a[0][0])
print(a[0][1])

print(a[1][0])
print(a[1][1])

print(a[1][1][1])
print(a[1][1][2])

print(a[0].copy())

a[0] = 89
print(a)

print('---------------Boolean indexing-----------------')
n = np.array(['ali', 'amin', 'mahsa', 'ali'])
print(n)

print(n == 'ali')

d = np.array([[1, 2, 3 ],
              [3, 4, 5],
              [6, 7, 8],
              [9, 10, 11]])
print(d)

print()

print(d[n == 'ali'])

print()

print(d[n == 'ali', 1:])

print()

print(d[ ~ (n == 'ali') ])

print()

c = n == 'ali'
print(d[~c])

print()

m = (n == 'ali') | (n == 'amin')
print(d[m])

d[d < 5] = 0
print(d)

print('---------------Fancy indexing-----------------')

arr = np.empty((7, 5))
for i in range(7):
    arr[i] = 5 * i

print(arr)

print()
print(arr[[3, 6, 0]])

print()
print(arr[[-7, -1]])

x = np.arange(35).reshape((7, 5))
print(x)

print(x[[1, 5, 6, 2], [0, 3, 1, 2]])

print()
print(x[[2, 6]][:,[0, 3, 1]])

print('---------------Transposing array and swapping axes-----------------')

arr = np.arange(8).reshape((2, 4))
print(arr)

print(arr.T)

z = np.arange(60).reshape((3, 4, 5))
print(z)

print(z.swapaxes(0, 1))
print(z.transpose(1, 0, 2))

print('---------------Universal Function: Ufunc-----------------')

arr = np.arange(4)
print(arr)

print(np.sqrt(arr))
print(np.exp(arr))

x = [2.6, 8.5, -9]
r, w = np.modf(x)
print(r, w)

x = np.array([1, 5, 10])
y = np.array([10, 2, 9])

print(np.maximum(x, y))

print('---------------where-----------------')

arr1 = np.array([1, 5, 8])
arr2 = np.array([4, 7 ,12])
cond = np.array([True, False, True])

r = [(x if c else y) for x, y, c in zip(arr1, arr2, cond)]
print(r)

res = np.where(cond, arr1, arr2)
print(res)

x = np.random.randn(2, 3)
print(x)

print(x>0)

print(np.where(x>0, 1, 0))

score = np.array([[7, 12, 20],[10, 15, 4]])
print(np.where(score>9, score, 10))

x = [[1, 2],[3, 4]]
y = [[5, 6],[7, 8]]
c = [[True, False],[False, True]]

print(np.where(c, x, y))

print('---------------Mathematical and Statistical Methods-----------------')

#amin, amx, mean, average, nanmean

arr = np.array([1, 5, 8, 6])
print(np.amin(arr))
print(np.amax(arr))
print(np.mean(arr))
print(np.average(arr, weights=[1, 2, 3, 4]))

print(np.nan)

x = np.array([1, 5, np.nan, 8, 6, np.nan, 7])
print(np.mean(x))
print(np.nanmean(x))

print('---------------Var, Std, median, quantile, percentile-----------------')

arr = np.array([1, 5, 8, 6, 10, 14, 1, 2 ,3])
print(np.var(arr))
print(np.std(arr))
print(np.median(arr))
print(np.sort(arr))
print(np.quantile(arr, 0.25))
print(np.quantile(arr, 0.5))
print(np.quantile(arr, 0.75))
print(np.percentile(arr, 25))
print(np.percentile(arr, 50))
print(np.percentile(arr, 75))

#sum, cumsum
arr = np.array([1, 5, 8, 6, 10, 14, 1, 2 ,3])
print(np.sum(arr))
print(np.cumsum(arr))

arr = np.array([[1, 5, 8], [6, 10, 14], [1, 2 ,3]])
print(arr)
print(np.sum(arr))
print(np.sum(arr, axis=0))
print(np.sum(arr, axis=1))
print(np.cumsum(arr, axis=0))
print(np.cumsum(arr, axis=1))

#all, any

x = np.array([False, False, False])
print(x.any())
print(x.all())

b = [0, 2, -3]
print(np.all(b))
print(np.any(b))

print('---------------Unique-----------------')

arr = np.array([1, 5, 2, 8, 6, 5, 10, 14, 1, 2 ,3])
print(np.unique(arr))
a, i = np.unique(arr, return_index=True)
print(a, i)

print('---------------Sort-----------------')

print(np.sort([1, 5, 2, 8, 6, 5, 10, 14, 1, 2 ,3]))

data = [('ali', 12.5, 35),('amin', 18.75, 27),('sara', 16.25, 27)]
# print(np.sort(data))

d = [('name', 'S10'), ('score', float), ('age', int)]
arr = np.array(data, dtype=d)

print(np.sort(arr, order='age'))
print(np.sort(arr, order='score'))

print('---------------in1d-----------------')

x = np.array([1, 5, 2, 8, 6, 4, 5, 10, 14, 1, 2 ,3])
y = [3, 4, 7]
print(np.in1d(x,y))

m = np.in1d(x,y, invert=True)
print(m)
print(x[m])

print('---------------Save & load-----------------')
x = np.array([1, 5, 2, 8, 6, 4, 5, 10, 14, 1, 2 ,3])
np.save('test.npy', x)
y = np.load('test.npy')
print(y)

with open('test.npy', 'wb') as f:
    np.save(f, x)

with open('test.npy', 'rb') as f:
    y = np.load(f)

arr1 = np.array([1, 5, 2])
arr2 = np.array([3, 6, 7])

np.savez('test2.npz', x = arr1, y = arr2)

t = np.load('test2.npz')
print(t['x'])
print(t['y'])
print(t.files)

print('---------------random_sample U[a, b): (b-a) * random_sample(...) + a-----------------')
#U[1, 20)
print(19 * np.random.random_sample(5) +1)

print('---------------rand: U[0, 1)-----------------')
print(np.random.rand(5))

print('---------------randint-----------------')
print(np.random.randint(0, 11, 7))

print('---------------randn: N(mu, sigma^2): sigma * rand(...) + mu-----------------')
mu = 5
sigma = 0.8
s = np.random.normal(mu, sigma, 5000)

# import matplotlib.pyplot as plt
# plt.hist(s, 30, density = True)
# plt.show()

np.random.seed(1324)
print(np.random.normal(size = 5))

print('---------------inner, outer, dot-----------------')

a = np.array([1, 5, 2])
b = np.array([3, 6, 7])
# 1 * 3 + 5 * 6 + 2 * 7 = 47
print(np.inner(a, b))
print(np.outer(a, b))

print()
x = np.array([[1, 2],[3, 7]])
y = np.array([[3,7],[1, 9]])

print(np.dot(x, y))

print('--------------------------------')

x = np.array([[1, 2],[3, 7]])

from numpy.linalg import inv, qr
print(inv(x))

b = x.T.dot(x)

i = inv(b)

print(b.dot(i))

print()

q, r = qr(b)
print(q)
print(r)


#  دانشگاه شهید مدنی آذربایجان
#  برنامه نویسی مقدماتی با پایتون
#  امین گلزاری اسکوئی
# https://github.com/Amin-Golzari-Oskouei/Python-Programming-Course-Basic-2021
# https://drive.google.com/drive/folders/1ZsQjBJJ4UAAp9zrGxm3c4qrhnvGBUYHw






