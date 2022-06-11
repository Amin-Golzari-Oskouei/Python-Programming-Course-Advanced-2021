#Merge

import pandas as pd
import numpy as np

print('------------merging Datasets-------------')
df1 = pd.DataFrame({'Name': ['ali', 'taha', 'sara'], 'C++':[18, 12, 17]})
print(df1)

print('--------')

df2 = pd.DataFrame({'Name': ['ali', 'taha', 'omid'], 'Python':[13, 14, 16]})
print(df2)

print('--------')

print(df1.merge(df2, on = 'Name'))

print('--------')

print(df1.merge(df2, how='inner', on = 'Name'))

print('--------')

print(df1.merge(df2, how='outer', on = 'Name'))

print('--------')

print(df1.merge(df2, how='left', on = 'Name'))

print('--------')

print(df1.merge(df2, how='right', on = 'Name'))

print('--------')

df1 = pd.DataFrame({'X': ['ali', 'taha', 'sara', 'ali'], 'V':[1, 3, 2, 5]})
print(df1)

print('--------')

df2 = pd.DataFrame({'Y': ['ali', 'taha', 'sara', 'ali'], 'V':[5, 7, 6, 8]})
print(df2)

print('--------')

print(df1.merge(df2, left_on = 'X', right_on='Y'))

print('--------')

print(df1.merge(df2, left_on = 'X', right_on='Y', suffixes=('_df1', '_df2')))

print('--------')

df1 = pd.DataFrame({'X': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'Y': [0, 1, 2, 3, 4, 5 ,6]})
print(df1)

print('--------')

df2 = pd.DataFrame({'X': ['a', 'b', 'd'], 'Z': [0, 1, 2]})
print(df2)

print('--------')

print(df1.merge(df2, on='X'))

print('--------')

print(df1.merge(df2))

print('--------')

print(df1.merge(df2, how='outer'))

print('--------')

df1 = pd.DataFrame({'A': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'B': [0, 1, 2, 3, 4, 5 ,6]})
print(df1)

print('--------')

df2 = pd.DataFrame({'C': ['a', 'b', 'd'], 'D': [0, 1, 2]})
print(df2)

print('--------')

print(pd.merge(df1, df2, left_on='A', right_on='C'))

print('--------')

df1 = pd.DataFrame({'X': ['b', 'b', 'a', 'c', 'a', 'b'], 'Y': [0, 1, 2, 3, 4, 5]})
print(df1)

print('--------')

df2 = pd.DataFrame({'X': ['a', 'b', 'a', 'b', 'd'], 'Z': [0, 1, 2, 3, 4]})
print(df2)

print('--------')

print(pd.merge(df1, df2))

print('--------')

print(pd.merge(df1, df2, how='left'))

print('--------')

print(pd.merge(df1, df2, how='right'))

print('--------')

df1 = pd.DataFrame({'K1': ['foo', 'foo', 'bar'], 'K2':['one', 'two', 'one'], 'Z':[1, 2, 3]})
print(df1)

print('--------')

df2 = pd.DataFrame({'K1': ['foo', 'foo', 'bar', 'bar'], 'K2':['one', 'one', 'one', 'two'], 'W':[4, 5, 6, 7]})
print(df2)

print('--------')

print(pd.merge(df1, df2,  on=['K1', 'K2'], how='outer'))

print('--------')

print(pd.merge(df1, df2,  on='K1', suffixes=('_df1', '_df2')))

print('------------merging on index-------------')

df1 = pd.DataFrame({'X': ['a', 'b', 'a', 'a', 'b', 'c'], 'Y': [0, 1, 2, 3, 4, 5]})
print(df1)

print('--------')

df2 = pd.DataFrame({'Z': [18, 15]}, index = ['a', 'b'])
print(df2)

print('--------')

print(pd.merge(df1, df2, left_on='X', right_index=True))

print('--------')

print(pd.merge(df1, df2, left_on='X', right_index=True, how='outer'))

print('--------')
d = {'X': ['H', 'H', 'H', 'N', 'N'], 'Y': [1397, 1398, 1399, 1398, 1399], 'Z': [0.0, 1.0, 2.0, 3.0, 4.0]}
df1 = pd.DataFrame(d)
print(df1)

print('--------')

i = [['N', 'N', 'H', 'H', 'H', 'H'],[1398, 1397, 1397, 1397, 1398, 1399]]
df2 = pd.DataFrame(np.arange(12).reshape((6, 2)), index=i, columns=['A', 'B'])
print(df2)

print('--------')

print(pd.merge(df1, df2, left_on=['X', 'Y'], right_index=True))

print('--------')

print(pd.merge(df1, df2, left_on=['X', 'Y'], right_index=True, how='outer'))

print('------------join-------------')

df1 = pd.DataFrame([[19, 12],[13, 18],[5, 16]], index=['ali', 'sara', 'taha'], columns=['C++', 'python'])
print(df1)

print('--------')

df2 = pd.DataFrame([[17, 12],[19, 20],[11, 6],[13, 18]], index=['farid', 'sara', 'mahsa', 'taha'], columns=['Java', 'PHP'])
print(df2)

# df1.merge(df2)

print('--------')

print(df1.merge(df2, left_index=True, right_index=True))

print('--------')

print(df1.join(df2))

print('--------')

print(df2.join(df1))

print('--------')

print(df2.join(df1, how='outer'))

print('--------')

df3 = pd.DataFrame([[15, 6],[17, 18],[19, 20],[3, 9]], index=['ali', 'sara', 'taha', 'fardi'], columns=['Pascal', 'C#'])
print(df3)

print('--------')

x = df2.join(df3, how='outer')
print(df1.join(x))

print('--------')

print(df1.join([df2, df3]))

print('------------concat-------------')

print(df1)

print('--------')

print(df2)

print('--------')

print(pd.concat([df1, df2]))

print('--------')

print(pd.concat([df1, df2], axis=1))

print('--------')

s1 = pd.Series([13, 20], index=['ali', 'sara'])
print(s1)

print('--------')

s2 = pd.Series([14, 15, 17], index=['taha', 'mahsa', 'sara'])
print(s2)

print('--------')

print(pd.concat([s1, s2], axis=1))

print('--------')

print(pd.concat([s1, s2], axis=1, keys=['C++', 'python']))

print('--------')

print(pd.concat([s1, s2], keys=['C++', 'python']))

print('--------')

r = pd.concat([s1, s2], keys=['C++', 'python'])

print(r.unstack())

print('------------combine_first-------------')

df1 = pd.DataFrame({'C++': [None, 12], 'python':[None, 14]}, index= ['ali', 'taha'])
print(df1)

print('--------')

df2 = pd.DataFrame({'C++': [None, 15], 'python':[12, None]}, index= ['ali', 'taha'])
print(df2)

print('--------')

print(df1.combine_first(df2))

print('--------')

print(df2.combine_first(df1))

print('--------')

df1 = pd.DataFrame({'C++': [None, 12], 'python':[14, None]}, index= ['ali', 'taha'])
print(df1)

print('--------')

df2 = pd.DataFrame({'python':[13, 20, None], 'Java':[None, 11, 17]}, index= ['ali', 'taha', 'Mahsa'])
print(df2)

print('--------')

print(df1.combine_first(df2))

print('------------pivot-------------')

df = pd.DataFrame({'A':['one', 'one', 'one', 'two', 'two', 'two'],
                   'B':[1, 1, 2, 1, 1, 2],
                   'C':[1, 2, 1, 2, 1, 2],
                   'V':[0, 1, 2, 3, 4, 5]})

print(df)

print('--------')

print(df.pivot(index='A', columns=['B', 'C'], values='V'))


print('--------')

print(df.pivot(columns='C', index=['A', 'B'], values='V'))

print('------------melt-------------')

df1 = pd.DataFrame({'Name': ['ali', 'taha', 'sara'], 'C++':[18, 12, 17], 'python':[14, 17, 12]})
print(df1)

print('--------')

print(df1.melt(['Name']))

print('--------')

m = pd.melt(df1, ['Name'])
r = m.pivot('Name', 'variable', 'value')
print(r)

print('--------')

print(r.reset_index())

print('--------')

print(df1)

print('--------')

print(df1.melt(['Name'], value_vars=['C++'], var_name='dars', value_name='score'))

print('--------')

print(df1.melt(['Name'], value_vars=['C++']))

#  دانشگاه شهید مدنی آذربایجان
#  برنامه نویسی مقدماتی با پایتون
#  امین گلزاری اسکوئی
# https://github.com/Amin-Golzari-Oskouei/Python-Programming-Course-Basic-2021
# https://drive.google.com/drive/folders/1ZsQjBJJ4UAAp9zrGxm3c4qrhnvGBUYHw

