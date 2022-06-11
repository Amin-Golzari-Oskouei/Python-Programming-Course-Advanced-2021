#Data Cleaning

import pandas as pd
import numpy as np

print('----------Handling Missing Data-------------')

from numpy import nan as NA

s = pd.Series([3, NA, 8, NA, 5])

print(s.notnull())

print('--------')

myser = s[s.notnull()]
print(myser)

print('--------')

print(s.dropna())

print('--------')

df = pd.DataFrame([[3, 9, 5],[4, NA, NA],[NA, NA, NA],[NA, 8, 6]])
print(df)

print('--------')

clean = df.dropna()
print(clean)

print('--------')

clean = df.dropna(how='all')
print(clean)

print('--------')

df[4] = NA
print(df)

print('--------')

clean = df.dropna(axis = 1, how='all')
print(clean)

print('--------')
df = pd.DataFrame([[14, NA, NA],[12, NA, NA],[18, NA, 14],[18, NA, 16],[15, 12, 19],[13, 1, 6]])
print(df)

print('--------')
clean = df.dropna()
print(clean)

print('--------')
clean = df.dropna(thresh=2)
print(clean)

print('----------fillna-------------')

frame = df.fillna(0)
print(frame)

print('--------')
frame = df.fillna({1:0 , 2:9})
print(frame)

print('--------')
print(df)
df.fillna(0, inplace=True)

print('--------')
print(df)

print('--------')
df = pd.DataFrame([[15, 12, 19],[12, 1, 6],[18, NA, 14],[18, NA, 16],[15, NA, NA],[13, NA, NA]])
print(df)

print('--------')

print(df.fillna(method='ffill'))

print('--------')

print(df.fillna(method='ffill', limit=3))

print('--------')

s= pd.Series([6, NA, 4, NA, 5])
print(s.mean())
print(s.fillna(s.mean()))

print('----------drop_duplicateds-------------')
frame = pd.DataFrame({'col1': ['a', 'b', 'a', 'b', 'a', 'b', 'b'],
                      'col2':[1 ,1 ,2 ,3 ,3 ,4 ,4]})
print(frame)

print('--------')

print(frame.duplicated())

print('--------')

print(frame.drop_duplicates())

print('--------')

print(frame.drop_duplicates(['col1']))

print('--------')

print(frame.drop_duplicates(['col1'], keep='last'))

print('--------')

print(frame.drop_duplicates(['col2'], keep='last'))

print('----------replace-------------')

myser = pd.Series([6, 4, 18, 17, 4, 13, 5])

print(myser.replace(4, np.nan))

print('--------')

print(myser.replace({4: np.nan, 18:0}))

print('--------')

print(myser.replace([4, 18], [np.nan, 0]))

print('----------cut-------------')

score = [20, 8, 17, 10]
bins = [0, 9, 15, 20]

c = pd.cut(score, bins)
print(c.categories)
print(c)
print(c.codes)
print(pd.value_counts(c))

print('--------')

score = [20, 8, 17, 10]
bins = [0, 9, 15, 20]

x = pd.cut(score, bins, labels=['bad', 'medium', 'good'])
print(x)
print(pd.value_counts(x))

print('--------')

ages = [20, 58, 27, 72, 100]
bins = [18, 25, 35, 60, 110]

x = pd.cut(ages, bins, labels=['Youth', 'YoungAdult', 'MiddleAged', 'senior'])
print(x)
print(pd.value_counts(x))


print('----------Detecting Outiers-------------')

df = pd.DataFrame(np.random.randn(1000, 3))
print(df.describe())

print(df.head())

print('--------')

s = np.sign(df)
print(s.head())

print('--------')

df[np.abs(df) > 3] = 3 * s
print(df.describe())

print('----------take-------------')

df = pd.DataFrame(np.arange(12).reshape((4, 3)))
print(df)

print('--------')

p = np.random.permutation(4)
print(p)

print('--------')

print(df.take(p))


print('----------sample-------------')

df = pd.DataFrame(np.arange(30).reshape((6, 5)))
print(df)

print('--------')

print(df.sample(n = 2))

print('--------')

myser = pd.Series([6, 4, 18, 17, 4, 13, 5])

print(myser.sample(n = 2))

print('--------')

print(df.sample(n = 2, random_state=1))

print('--------')

df = pd.DataFrame(np.arange(12).reshape((4, 3)), columns=['F1', 'F2', 'F3'], index=['s1', 's2', 's3', 's4'])
print(df)

print('--------')

print(df.sample(n = 2, weights = 'F3',  random_state=1))

print('--------')

s = pd.Series([15, 7, 12, 16])
print(s.sample(n = 6 , replace=True))

print('--------')

print(df.sample(frac=0.5))

print('--------')

print(df.sample(frac=2, replace=True))

print('--------')

print(df['F1'].sample(n = 3))

print('----------get_dummies-------------')
s = pd.Series(list('abca'))
print(s)

print('--------')

df = pd.get_dummies(s)
print(df)

print('--------')

s = pd.Series(list('abcaa'))
df = pd.get_dummies(s)
print(df)

print('--------')

lst = ['a', 'b', np.nan]
print(pd.get_dummies(lst))

print('--------')

df = pd.DataFrame({'F1':['a', 'b', 'c'],
                   'F2':['b', 'a', 'a'],
                   'F3':[7, 2, 3]})
print(df)

print('--------')

print(type(df['F1']))

print('--------')

print(pd.get_dummies(df['F1']))

print('--------')

print(pd.get_dummies(df))

print('--------')

print(pd.get_dummies(df, prefix=['col1', 'col2']))

print('--------')

d = pd.get_dummies(df['F1'])
print(d)

print('--------')

print(df)

print('--------')
dfdummy = df[['F2', 'F3']].join(d)
print(dfdummy)

#  دانشگاه شهید مدنی آذربایجان
#  برنامه نویسی مقدماتی با پایتون
#  امین گلزاری اسکوئی
# https://github.com/Amin-Golzari-Oskouei/Python-Programming-Course-Basic-2021
# https://drive.google.com/drive/folders/1ZsQjBJJ4UAAp9zrGxm3c4qrhnvGBUYHw

