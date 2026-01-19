#used to reshape panda file

#melt 

import pandas as pd
var=pd.DataFrame({"days":[1,2,3,4],"eng":[3,4,2,1],"math":[4,6,3,2]})
print(var)    #display table horizontally

print(pd.melt(var))    #display table vertically

print(pd.melt(var,id_vars=["days"])) #it give id means index to dataframe

print(pd.melt(var,id_vars=["days"],var_name="python",value_name="wscude"))  #to give name to variable and value in dataframe

#pivot 

#used for data arrangement

var1=pd.DataFrame({"days":[1,2,3,4],"stu_name":["a","b","c"],eng":[3,4,2,1],"math":[4,6,3,2]})
print(var1)