import pandas as pd

var1=pd.DataFrame({'a':[1,2,3],'b':[4,5,6]},index=['a','b','c'])   #give index to the dataframe
var2=pd.DataFrame({'c':[11,22,33],'d':[44,55,66]},index=['a','b','c'])
print(var1.join(var2))        #it will join var2 after var1 ie. a b c d

var3=pd.DataFrame({'a':[1,2,3],'b':[4,5,6]})
var4=pd.DataFrame({'c':[11,22],'d':[44,55]})
print(var3.join(var4))        #at remaining place it will give naN
  
print(var4.join(var3))        #it will join according to var4
 
print(var4.join(var3,how='inner'))  #inner=intersection

print(var4.join(var3,how='outer'))   #outer=union

print(var4.join(var3,how='left'))     #left=join according to left dataframe

print(var4.join(var3,how='right'))   #right=join according to right dataframe


#Append

va1=pd.DataFrame({'a':[1,2,3],'b':[4,5,6]})
va2=pd.DataFrame({'c':[11,22,33],'d':[44,55,66]})
print(va1.append(va2))







