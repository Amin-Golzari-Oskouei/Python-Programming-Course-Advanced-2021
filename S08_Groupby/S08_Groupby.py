#GroupBy

import pandas as pd
import numpy as np

city = ['Kermanshah', 'Hamedan', 'Oromieh', 'Mashhad', 'Yazd', 'Kerman', 'Zabol']

myser = pd.Series([2, 3, 1, 6, 4, 5, 1], index=city)
print(myser)

print('----------')

k = ['W','W','W','E','E','E','E']
print(myser.groupby(k).max())

print('----------')

myser[['Oromieh', 'Yazd', 'Zabol']] = np.nan
print(myser)

print('----------')

print(myser.groupby(k).mean())

print('----------')

f = lambda g: g.fillna(g.mean())
print(myser.groupby(k).apply(f))

print('----------')

f = {'W': 1, 'E': 2}
c = lambda g: g.fillna(f[g.name])
print(myser.groupby(k).apply(c))

print('-------------------------------')

df = pd.DataFrame({'key1': ['ali','ali','ali','sara','sara','sara','sara'],
                   'key2': ['one','one','two','one','one','two','two'],
                   'data': [12, 16, 13, 20, 8, 17, 10]})

print(df)

print('----------')

g = df.groupby('key1')

print('----------')

print(g.describe())

print('----------')

print(g.max())

print('----------')

print(g.min())

print('----------')

def f(t):
    return t.max() - t.min()

print(g.agg(f))

print('----------')

print(df)

print('----------')

d = dict(list(df.groupby('key1')))
print(d['ali'])

print('----------')

print(df['data'].groupby(df['key1']).min())

print('----------')

print(df)

print('----------')

h = df.groupby(['key1', 'key2'])
print(h.max())

print('--------------Grouping by index levels---------------')

arr = np.array([[11, 12, 16, 4, 15],
                [17, 2, 18, 19, 10],
                [7, 15, 13, 14, 11],
                [8, 17, 13, 20, 12]])

mi = pd.MultiIndex.from_arrays([['ali', 'ali', 'ali','sara', 'sara'],
                                [1, 2, 3, 1, 2]],
                                names = ['X', 'Y'])
print(mi)

print('----------')

mydf = pd.DataFrame(arr, columns=mi)
print(mydf)

print('----------')

print(mydf.groupby(level='X', axis=1).max())

print('--------------cut----------------')

Score = [16, 12, 13, 14, 20, 16, 17, 5, 19, 7]
sc = pd.cut(Score, 4, labels=['Q1', 'Q2', 'Q3','Q4'])
print(sc)

print('----------')


S1 = pd.Series(Score)
S2 = pd.Series(sc)

print(S1.groupby(S2).agg(['min', 'count']).reset_index())


print('------------------------------')

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [11, 12, 13, 14, 15, 16, 17, 18, 19]

df =  pd.DataFrame({'Col1': a, 'Col2': b})
print(df)

print('----------')

q = pd.cut(df.Col1, 4)
print(q)

print('----------')

def myfunc(g):
    return {'Max': g.max(), 'Count': g.count()}

g = df.Col2.groupby(q)
print(g.apply(myfunc).unstack())

print('--------------transform----------------')

n = ['ali','ali','ali','ali','sara','sara','sara','taha', 'taha']
s = [11, 20, 13, 14, 15, 6, 12, 18, 19]

df = pd.DataFrame({'Name': n, 'Score': s})
print(df)

print('----------')

g = df.groupby('Name').Score

print(g.max())

print('----------')

print(g.min())

print('----------')

print(g.count())

print('----------')

print(g.transform('max'))

print('----------')

print(g.transform(lambda x: x-1))

print('----------')

print((df['Score'] - g.transform('mean')) / g.transform('std'))

print('--------------Example----------------')

df = pd.read_csv('iris.csv')
print(df)

print('----------')

print(df.groupby(['variety']).agg('min'))

print('----------')

def myfunc(f, n = 5):
    return f.sort_values(by = 'sepal.length')[:n]

print(myfunc(df, 8))

print('----------')

print(df.groupby(['variety']).apply(myfunc))

print('--------------Category----------------')

t = df['variety']
print(t)

print('----------')

c = t.astype('category')
print(c)

print('----------')

print(c.values.codes)

print('----------')

print(c.value_counts())

print('----------')

print(c.values.categories)

print('----------')

print(c.isin(['Setosa']))

print('----------')

x = c[c.isin(['Setosa'])]
print(x)

print('----------')

y = x.cat.remove_unused_categories()
print(y)


#  دانشگاه شهید مدنی آذربایجان
#  برنامه نویسی مقدماتی با پایتون
#  امین گلزاری اسکوئی
# https://github.com/Amin-Golzari-Oskouei/Python-Programming-Course-Basic-2021
# https://drive.google.com/drive/folders/1ZsQjBJJ4UAAp9zrGxm3c4qrhnvGBUYHw


