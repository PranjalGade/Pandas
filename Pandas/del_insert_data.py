import pandas as pd

#insert
var=pd.DataFrame({'a':[1,2,3,4],'b':[2,2,1,3]})
print(var)
var.insert(1,'python',var['a'])
print(var)


#delete
var1=var.pop('b')
print(var1)

del var['a']
print(var)