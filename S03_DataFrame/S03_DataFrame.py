#pandas: DataFrame

import pandas as pd
import numpy as np

score = [[12, 20, 18], [13, 14, 6], [12, 8, 19], [20, 16, 14]]

df = pd.DataFrame(data=score)
print(df)

dars = ['Python', 'C++', 'Java']
name = ['Ali', 'Sara', 'Taha', 'Mahsa']

df = pd.DataFrame(data=score, index = name, columns=dars)
print(df)

d = {'Python': [12, 13, 12, 20], 'C++': [20, 14, 8, 16], 'Java':[18, 6, 19, 14]}
stu = pd.DataFrame(data=d, index=name)
print(stu)

print('--------------------------------------')

print(df.values)

print(df.columns)
print('Java' in df.columns)

print(df.index)
print('Mahsa' in df.index)

print(df.axes)

print(df.dtypes)

print('------------------Indexing, Selection, and filtering--------------------')

print(df)

print('---------')
print(df['C++'])

print('---------')
print(df[['Java','C++']])

print('---------')
print(df[['C++','Java']])

print('---------')
print(df[:3])

print('---------')
print(df[1:3])

print('---------')
print(df < 10)

print('---------')
df[df < 10] = 0
print(df)

print('---------')
print(df[df['C++'] > 10])

print('----------loc, iloc---------')

print(df)

print('---------')
print(df.loc['Taha'])

print('---------')
print(df.iloc[2])

print('---------')
print(df.loc['Taha', ['Python','Java']])

print('---------')
print(df.iloc[[2], [0, 2]])

print('---------')
print(df.iloc[2, [0, 2]])

print('---------')
print(df.loc[:'Taha', ['Python']])

print('---------')
print(df.iloc[:3, 0])

print('---------')
print(df.iloc[:2, [0, 1]])

print('---------')
print(df.iloc[0, 1])

print('---------')
print(df.iloc[[0, 1]])

print('---------')
print(df.iloc[[False, False, True, True]])

print('---------')
print(df.iloc[:, [True, False, True]])

print('---------')
print(df.iloc[[False, False, True, True], [True, False, True]])

print('----------iat---------')

print(df)
print(df.iat[2, 1])
print(df.iat[0, 1])

print('----------reindex---------')

print(df)

print('---------')
print(df.reindex(['Ali', 'Sara', 'Taha', 'Mahsa', 'Omid']))

print('---------')
print(df.reindex(['Ali', 'Sara', 'Taha', 'Mahsa', 'Omid'], fill_value=0))

print('---------')
print(df.reindex(columns = ['Python', 'C++', 'Java', 'pascal']))

print('---------')
print(df.reindex(columns = ['Python', 'C++', 'Java', 'pascal'], fill_value=0))

print('----------Sort_values---------')

print(df)

print('---------')
print(df.sort_values(by = 'Python'))

print('---------')
print(df.sort_values(by = 'Python', ascending=False))

print('---------')
print(df.sort_values(by = ['Python', 'Java'], ascending=False))

print('----------Sort_index---------')

print(df)

print('---------')
print(df.sort_index())

print('---------')
print(df.sort_index(axis=1))

print('---------')
print(df.sort_index(axis=1, ascending=False))

print('----------idxmax---------')

print(df)

print('---------')
print(df.idxmax())

print('----------sum(), mean(), describe()---------')

print(df)

print('---------')
print(df.sum())

print('---------')
print(df.mean())

print('---------')
print(df.sum(axis='columns'))

print('---------')
print(df.mean(axis='columns'))

print('---------')

df2 = df.reindex(['Ali', 'Sara', 'Taha', 'Mahsa', 'Omid'])

print(df2)

print('---------')
print(df2.sum(axis='columns'))

print('---------')
print(df2.sum(axis='columns', skipna=False))

print('---------')
print(df.describe())

print('----------Transpose---------')

print(df.T)

print('----------apply---------')

print(df.apply(lambda x: x - 1))

print('---------')
print(df - 1)

print('---------')
def myfunc(x):
    return pd.Series([x.min(), x.max()], index=['min', 'max'])

print(df.apply(myfunc))

print('----------map---------')

print(df)

print('---------')
print(df['Python'].map(lambda x: x - 1))

print('----------applymap---------')

print(df)

print('---------')
print(df.applymap(lambda x: '%.4f' %x))

print('----------drop---------')

print(df)

print('---------')

a = df.drop(['Java'], axis=1)

print(a)

print('---------')

a = df.drop(['Mahsa'])

print(a)
print(df)

print('---------')

df.drop(['Mahsa'], inplace=True)
print(df)

print('----------empty---------')
print(df.empty)

print('----------Arithmetic methods with fill values---------')

arr1 = np.arange(12).reshape((4,3))

df1 = pd.DataFrame(data = arr1, columns=list('abc'))
print(df1)

print('---------')
arr2 = np.arange(10).reshape((5,2))

df2 = pd.DataFrame(data = arr2, columns=list('ab'))
print(df2)

print('---------')
df2.loc[1, 'b'] = np.nan
print(df2)

print('---------')
print(df1 + df2)

print('---------')
print(df1.add(df2))

print('---------')
print(df1.add(df2, fill_value = 0))

print('---------')
print(df1.sub(df2, fill_value = 0))

print('---------')
print(df1.cumsum())

print('----------index.name, columns.name---------')
mydic = {'City': ['Hamedan', 'Hamedan', 'Hamedan', 'Tehran', 'Tehran', 'Tehran'],
         'Year':[1396, 1397, 1398, 1397, 1398, 1399],
         'pop':[2, 2.2, 3, 8, 8.5, 9]}

frame = pd.DataFrame(data = mydic)
print(frame)

print('---------')
mydic = {'Tehran': {1397:8, 1398:8.5, 1399:9}, 'Hamedan': {1396:2, 1397:2.5, 1398:3} }

frame = pd.DataFrame(data = mydic)
print(frame)

print('---------')
frame.index.name = 'year'
frame.columns.name = 'City'
print(frame)

print('----------Operation between DataFrame and Series---------')

print(frame)

print('---------')
myser = frame.iloc[1]
print(myser)

print('---------')
print(frame + myser)

print('----------Hierachical Indexing---------')

frame = pd.DataFrame({'C++': [6, 7, 4, 16, 13, 15, 7, 14],
                      'Python':[3, 2, 5, 14, 19, 18, 16, 10],
                      'K1':['one','one','one','two','two','two','two','two'],
                      'K2':['ali', 'reza', 'sara', 'ali', 'reza', 'sara', 'taha', 'farid']})
print(frame)

print('---------')
df = frame.set_index(['K1', 'K2'])
print(df)

print('---------')
print(df.sort_index(level=1))

print('---------')
print(df.sort_index(level='K2'))

print('---------')
print(df)

print('---------')
print(df.unstack())

print('---------')
print(df.swaplevel('K1','K2'))

print('---------')

d = np.arange(12).reshape((4, 3))
c = [['ohio', 'ohio', 'colorado'], ['green', 'red', 'green']]
i = [['a', 'a', 'b', 'b'], [1, 2, 1, 2]]

frame= pd.DataFrame(data=d, index=i, columns=c)
print(frame)

print('---------')
frame.index.names = ['Key1','Key2']
frame.columns.names = ['State','Color']
print(frame)

#  دانشگاه شهید مدنی آذربایجان
#  برنامه نویسی مقدماتی با پایتون
#  امین گلزاری اسکوئی
# https://github.com/Amin-Golzari-Oskouei/Python-Programming-Course-Basic-2021
# https://drive.google.com/drive/folders/1ZsQjBJJ4UAAp9zrGxm3c4qrhnvGBUYHw
