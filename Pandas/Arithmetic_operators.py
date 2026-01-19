import pandas as pd
var=pd.DataFrame({'a':[1,2,3,4],'b':[2,4,2,1]})
print(var)
var['c']=var['a']+var['b']                  #addition
print(var)


var1=pd.DataFrame({'a':[1,2,3,4],'b':[2,4,2,1]})
print(var1)
var1['c']=var1['a']-var1['b']                  #subtraction
print(var1)


var2=pd.DataFrame({'a':[1,2,3,4],'b':[2,4,2,1]})
print(var2)
var2['c']=var2['a']*var2['b']                  #multiply
print(var2)


var3=pd.DataFrame({'a':[1,2,3,4],'b':[2,4,2,1]})
print(var3)
var3['c']=var3['a']/var3['b']                  #divide
print(var3)