import pandas as pd
csv_1=pd.read_csv("C:\\Users\\pranj\\OneDrive\\Documents\\test_new.csv")
print(csv_1)

print(csv_1.index)                   #display starting and end+1 index

print(csv_1.columns)                 #display columns  

print(csv_1.head(2))                 #to diplay first 2 data

print(csv_1.tail(2))                 #to diplay last 2 data


print(csv_1[:2])                     #slice operation

print(type(csv_1))                   #type of csv file

print(csv_1.index.array)             #to display index into array

print(csv_1.to_numpy())              #converting into numpy array

print(csv_1.sort_index(axis=1))      # 0 means row wise ascending and 1 means column wise ascending

csv_1.loc[0,'b']=4                   # for updating value in csv file
print(csv_1)

csv_1.drop('a',axis=1)               #to drop the column
print(csv_1)