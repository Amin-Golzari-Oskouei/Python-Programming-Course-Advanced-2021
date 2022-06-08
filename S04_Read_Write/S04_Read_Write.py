# Data Loading, Storage
import json

import pandas as pd

mydata = {'name': ['Ali', 'Sara', 'Taha', 'Omid'],
          'age': [27, 24, 25, 26],
          'score': [19, 18, 20, 13]}

mydf = pd.DataFrame(mydata, columns=['name', 'age', 'score'])
print(mydf)

print('-----------CSV-------------')
mydf.to_csv('Files/score.csv', index = False)

print(pd.read_csv('Files/score.csv'))


print('-----------File without header-------------')

print(pd.read_csv('Files/score.csv'))

print('------')

print(pd.read_csv('Files/score.csv', header=None))

print('------')

print(pd.read_csv('Files/score.csv', names = ['name', 'python', 'C++', 'Java']))

print('-----------skiprows-------------')

print(pd.read_csv('Files/age.csv'))

print('------')

print(pd.read_csv('Files/age.csv', skiprows=[0]))

print('------')

print(pd.read_csv('Files/age.csv', header=[1]))

print('-----------csv.reader-------------')

import csv

with open('Files/score.csv') as f:
    x = list(csv.reader(f))

print(x)
print(x[0])
print(x[1:])

print('-----------read.table-------------')

print(pd.read_table('Files/score.csv'))

print('------')

print(pd.read_table('Files/score.csv', sep=','))

print('------')

print(pd.read_table('Files/mytext.txt', sep='\s+'))

print('-----------nrows, chunksize-------------')

path = 'Files/Alphabet.csv'

print(pd.read_csv(path))

print('------')

print(pd.read_csv(path, nrows=8))

print('------')

pd.options.display.max_rows = 10
print(pd.read_csv(path))

print('------')

print(pd.read_csv(path, skipfooter=22, engine='python'))

print('------')

c = pd.read_csv(path, chunksize=8)

for i in c:
    print(i)


print('-----------sys.stdout-------------')

import sys

mydata = pd.read_csv('Files/score.csv')

mydata.to_csv(sys.stdout)

print('------')

mydata.to_csv(sys.stdout , index=False, header=False, sep='|')

print('-----------df.to_excel-------------')

# pip install openyxl

print(mydf)

mydf.to_excel('Files/score.xlsx', index = False)

print(pd.read_excel('Files/score.xlsx'))

print('-----------JSON: JavaScript Object Notation-------------')

mystr = """ 
{
"FistName": "Taha",
"Courses": [{"name": "python", "score": 17},{"name": "C++", "score": 18}]
}
"""

mysict = json.loads(mystr)

frame = pd.DataFrame(mysict['Courses'], columns=['name', 'score'])
print(frame)

frame.to_json('Files/Course.json')
frame.to_json('Files/Course_values.json', orient='values')
frame.to_json('Files/Course_index.json', orient='index')
frame.to_json('Files/Course_split.json', orient='split')

print('-----------HTML-------------')
#pip install Lxml
#pip install html5lib

mystr = """
<table>
  <thead>
    <tr>
      <th>name</th>
      <th>score</th>
    </tr>
  </thead> 
  <tbody>
    <tr>
      <td>Ali</td>
      <td>12</td>
    </tr>
    <tr>
      <td>Sara</td>
      <td>18</td>
    </tr>    
   </tbody>   
</table>
"""

lst = pd.read_html('Files/test.html')
print(lst[0])

print('------')

print(lst[0].info())

print('------')

u = 'https://en.wikipedia.org/wiki/Minnesota'
x = pd.read_html(u , match='Election results from statewide races')
print(x[0])

print('-----------PKL file-------------')

frame = pd.read_csv('Files/score.csv')
print(frame)

print('------')

frame.to_pickle('Files/test.pkl')

print(pd.read_pickle('Files/test.pkl'))

print('-----------HDF-------------')
#pip install tables

import tables

mydf = pd.DataFrame({'A': [18, 20], 'B': [3, 15]})
print(mydf)

print('------')

path = 'Files/data.h5'

mydf.to_hdf(path, key='df', mode='w')

print(pd.read_hdf(path, key = 'df'))


print('-----------request.get-------------')
import requests

r = requests.get('https://api.github.com/repos/pandas-dev/pandas/issues')

if r.status_code == 200:
    print('OK')
elif r.status_code == 404:
    print('Not Found.')

df = pd.DataFrame(r.json(), columns=['number', 'title'])
print(df)


'''
to_csv read_csv

read_table

to_excel read_excel

to_json read_json

to_pickle read_pickle

to_hdf read_hdf

read_html
'''








