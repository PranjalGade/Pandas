#Merge

import pandas as pd
var=pd.DataFrame({'a':[1,2,3,4],'b':[1,2,3,4]})
var1=pd.DataFrame({'a':[11,22,33,44],'b':[1,2,3,4]})
print(pd.merge(var,var1,on='b'))


var2=pd.DataFrame({'a':[1,2,3,4],'b':[1,2,3,4]})
var3=pd.DataFrame({'a':[11,22,33,44],'b':[1,2,3,5]})
print(pd.merge(var2,var3,how="inner"))
print(pd.merge(var2,var3,how="left"))
print(pd.merge(var2,var3,how="right"))
print(pd.merge(var2,var3,how="outer"))


var=pd.DataFrame({'a':[1,2,3,4],'b':[1,2,3,4]})
var1=pd.DataFrame({'a':[11,22,33,44],'b':[1,2,3,4]})
print(pd.merge(var,var1,left_index=True,right_index=True,suffixes=("name","python")))   #it will display both data at same time

#concat

sr1=pd.Series([1,2,3,4])
sr2=pd.Series([5,6,7,8])
print(pd.concat([sr1,sr2]))

d1=pd.DataFrame({'a':[1,2,3,4],'b':[1,2,3,4]})
d2=pd.DataFrame({'a':[11,22,33,44],'b':[1,2,3,4]})
print(pd.concat([d1,d2]))
print(pd.concat([d1,d2],axis=1))        #concat column wise










