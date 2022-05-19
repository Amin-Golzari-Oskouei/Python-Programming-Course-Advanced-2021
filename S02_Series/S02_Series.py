# Series

# pip install pandas

import pandas as pd

s = pd.Series([12, 8, 19, 7])
print(s)

s = pd.Series([12, 8, 19, 7], index=['ali', 'taha', 'sara', 'omid'])
print(s)

s = s.reindex(['ali', 'taha', 'mahsa', 'omid'])
print(s)

print('--------------------------')

print(s[1])
print(s['mahsa'])
print(s['taha'])

s['mahsa'] = 20
print(s)

print(s.index)
print(s.values)

print('--------------------------')

print(s[1:3])

print()

print(s[:2])

print()

print(s.iloc[:2])

print('--------------------------')

s.index.name = 'name'
print(s)

s.name = 'score'
print(s)

print('--------------------------')

s = s.drop('omid')
print(s)

print()

s = s.drop(['mahsa', 'taha'])
print(s)

print('--------------------------')

myser = pd.Series([12, 4, 5, 7, 2], index=['a', 'b', 'c', 'd', 'e'])
print(myser)

print(myser.pop('c'))
print(myser)

print('--------------------------')

import numpy as np

s = pd. Series([12, 4, 5, np.nan, 7, 2], index=['a', 'b', 'c', 'd', 'e', 'f'])
print(s)

print(s.isna())
print(s.notna())

print('--------------------------')

s = pd. Series([12, 4, 5, np.nan, 7, 2], index=['a', 'b', 'c', 'd', 'e', 'f'])
print(s)

print(s.isin([5]))

print('--------------------------')

sc = s.copy()

s['b'] = 89
print(s)
print(sc)

print('--------------------------')

print(s.sort_values())
print(s.sort_index())
print(s.rank())

print('--------------------------')

s = pd. Series([12, 4, 5, np.nan, 7, 2], index=['a', 'b', 'c', 'a', 'e', 'b'])
print(s)
print(s['b'])
print(s.index.is_unique)
print(s.describe())
print(s.count())
print(s.quantile(0.5))
print(s.quantile([0.25, 0.75]))

print('--------------------------')

s = pd. Series([12, 4, 5, np.nan, 7, 2], index=['a', 'b', 'c', 'a', 'e', 'b'])

print(s >= 5)
print(s.where(s >= 5))

print('--------------------------')

myser = pd. Series(['a', 'b', 'a', 'c', 'd'])
print(myser.duplicated())
print(myser.drop_duplicates())

print('--------------------------')

s = pd. Series([1, 2, 3, 4])
print(s)
print(s.add_prefix('item_'))
print(s.add_suffix('_item'))

print('--------------------------')

a = pd. Series([1, 2, 3, 4])
b = pd. Series([5, 6, 7, 8])

print(a + b)
print(a.add(b))
print()
print(a - b)
print(a.subtract(b))
print()
print(a * b)
print(a.multiply(b))
print()
print(a.pow(b))
print()
print(a.divide(b))
print()
print(a.mod(b))

a = pd. Series([1, 2, 3], index=['a', 'b', 'c'])
b = pd. Series([5, 6, 7], index=['a', 'b', 'd'])
print(a.add(b))
print(a.add(b, fill_value = 0))

print('------------eq, ne, gt, ge, lt, le--------------')

a = pd. Series([5, 7, 12, 4])
b = pd. Series([5, 6, 7, 8])

print(a.eq(b))
print(a.ne(b))
print(a.gt(b))
print(a.lt(b))

print('------------argmax, argmin, idxmin, idxmax--------------')

score = pd.Series({'Java': 15, 'C++': 20, 'Python': 12, 'Pascal':9})
print(score)
print(score.argmax())
print(score.argmin())
print(score.idxmax())
print(score.idxmin())

print('------------cumsum, cumprod--------------')

s = pd. Series([12, 4, 5, np.nan, 7, 2])
print(s.cumsum())
print()
print(s.cumprod())

print('------------value_counts--------------')

myser = pd. Series(['a', 'b', 'a', 'c', 'd', 'd', 'b', 'a', 'e'])
print(myser.value_counts())
print()
print(pd.value_counts(myser.values, sort=False))

print('------------unique--------------')

myser = pd. Series(['a', 'b', 'a', 'c', 'd', 'd', 'b', 'a', 'e'])
print(myser.unique())
print(pd. Series(['a', 'b', 'a', 'c', 'd', 'd', 'b', 'a', 'e']).unique())

print('------------append--------------')

a = pd. Series([5, 7, 12, 4])
b = pd. Series([5, 6, 7, 8])

print(a.append(b))

b = pd. Series([5, 6, 7, 8], index=[4, 5, 6, 7])

print(a.append(b))

print('------------combine--------------')

s1 = pd.Series({'Java': 15, 'C++': 20, 'Python': 12, 'Pascal':9})
s2 = pd.Series({'Java': 17, 'C++': 14, 'Python': 17})

print(s1.combine(s2, max))
print(s1.combine(s2, max, fill_value=10))

print('------------apply--------------')

s = pd. Series([5, 7, 12, 100])
print(s.apply(np.log10))

def f(x):
    return x ** 2

print(s.apply(f))
print(s.apply(lambda x: x ** 2))

def h(x, y):
    return x - y

print(s.apply(h, args =(2,)))

def myfunc(r, **kwargs):
    for i in kwargs:
        r += kwargs[i]
    return r

print(s.apply(myfunc, x = 2, y = 4))

print('------------transform--------------')
s = pd. Series([5, 8, 12, 100])
print(s.transform([np.sqrt, np.log2]))

print('------------aggregate--------------')
s = pd. Series([5, 8, 12, 100])
print(s.agg(['min', 'max']))

print('------------nlagest--------------')
data = {'a': 6, 'b': 3, 'c': 8, 'e':5, 'f':9, 'g':3, 'w':5}

s = pd. Series(data)
print(s.nlargest())
print()
print(s.nlargest(4, keep='last'))
print()
print(s.nlargest(4, keep='all'))
print()
print(s.nsmallest())
print()
print(s.nsmallest(4, keep='last'))
print()
print(s.nsmallest(4, keep='all'))

print('------------groupby--------------')

i = ['BMW', 'BMW', 'Benz', 'Benz']
d = [220, 180, 230, 200]

s = pd.Series(d, index=i, name='MaxSpeed')
print(s)

print(s.groupby(i).max())
print(s.groupby(i).mean())

print('------------between--------------')
s = pd. Series([5, 20, 12, 100])
print(s.between(12, 20))

print('------------dropna--------------')
s = pd. Series([5, np.nan, 12, np.nan])
s.dropna(inplace=True)
print(s)

print('------------to_numpy--------------')
s = pd. Series([5, 20, 12, 100])
arr = s.to_numpy()
print(arr)
print(type(arr))

print('------------to_dict--------------')
s = pd. Series([5, 20, 12, 100])
d = s.to_dict()
print(d)
print(type(d))

print('------------replace--------------')
s = pd. Series([5, 20, 12, 100])
print(s.replace(5, 9))

print('------------repeat--------------')
s = pd. Series([5, 20, 5, 100])
print(s.repeat(3))

print('------------MultiIndex--------------')
lst = [['BMW', 'BMW', 'Benz', 'Benz'], ['A', 'B', 'A', 'B']]
mi = pd.MultiIndex.from_arrays(lst, names=('Machine', 'Class'))
d = [220, 180, 230, 200]
s = pd.Series(d, index=mi)
print(s)

print(s.groupby(level='Machine').max())
print(s.groupby(level=0).max())

print(s.groupby(level='Class').max())
print(s.groupby(level=1).max())


#  دانشگاه شهید مدنی آذربایجان
#  برنامه نویسی مقدماتی با پایتون
#  امین گلزاری اسکوئی
# https://github.com/Amin-Golzari-Oskouei/Python-Programming-Course-Basic-2021
# https://drive.google.com/drive/folders/1ZsQjBJJ4UAAp9zrGxm3c4qrhnvGBUYHw



















