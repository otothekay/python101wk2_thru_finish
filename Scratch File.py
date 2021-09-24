import json
import pandas as pd
import matplotlib.pyplot as plt  ## We will talk about plots next week

file_nm = 'Hawaii.json'
## json is a fundamental library that we are importing
## But first to uses json we have to open the file with 'open'
with open(file_nm) as json_data:
     data = json.load(json_data)
## Where is the data I want.
print(data.keys())
## What form is it in.
type(data['data'])  # A list!
print(data['data'][0])     # BUT NO HEADERS :-(
# ['row-mrk5-qh8e~w7em', '00000000-0000-0000-AF4D-4A5C32998A7B', 0, 1425775310, None, 1425775310, None, '{ }', '1960', '94.6', None]
df_json = pd.DataFrame(data['data'])  ## We only want the last three columns
A = df_json.iloc[:,-3:]
A = A.rename(columns={8:'Year', 9:'Fuel Consumption',10:'Fuel Expenditures'})
A.plot(x='Year', y='Fuel Consumption')  # ERROR What!!!
print(A.dtypes)   # Our values are not numbers!
A['Year'] = A['Year'].astype(int)
A['Fuel Consumption'] = A['Fuel Consumption'].astype(float)
A.plot(x='Year', y='Fuel Consumption')
plt.show()

