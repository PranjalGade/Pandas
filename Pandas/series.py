import pandas as pd
a=pd.Series([1,2,3,4,5])
print(a)
print(type(a))
print(a[2])


x=[1,2,3,2]
var=pd.Series(x,index=['a','b','c','d'],dtype='float',name='python')
print(var)

#dictionary
dic={"name":['c','c++','java'],"por":[11,12,12],"rank":[1,3,2]}
var1=pd.Series(dic)
print(var1)

v1=pd.Series(12)
print(v1)

v2=pd.Series(12,index=[1,2,4,2,1,3])
print(v2)