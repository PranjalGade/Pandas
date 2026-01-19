import pandas as pd
var=pd.DataFrame([1,2,3,4])
print(var)


a={'a':[1,2,3,4,5],'s':[1,2,3,4,5]}           #dictionary
var1=pd.DataFrame(a)

var2=pd.DataFrame(a,columns=['a'])        #it give only one column

print(var1['s'][2])                      #find specific digit

print(var1)



list1=[[1,2,3,4],[11,12,13,14]]           #list within list
var=pd.DataFrame(list1)
print(var)