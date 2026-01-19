import pandas as pd
csv_1=pd.read_csv("C:\\Users\\pranj\\OneDrive\\Documents\\test_new.csv")
print(csv_1)

csv_2=pd.read_csv("C:\\Users\\pranj\\OneDrive\\Documents\\test_new.csv",nrows=2)
print(csv_2)

csv_3=pd.read_csv("C:\\Users\\pranj\\OneDrive\\Documents\\test_new.csv",usecols=['b','c'])
print(csv_3)

csv_4=pd.read_csv("C:\\Users\\pranj\\OneDrive\\Documents\\test_new.csv",skiprows=[0])
print(csv_4)

csv_5=pd.read_csv("C:\\Users\\pranj\\OneDrive\\Documents\\test_new.csv",names=['col1','col2','col3','col4'])
print(csv_5)