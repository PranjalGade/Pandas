import pandas as pd
var=pd.DataFrame({'name':['a','d','c','c','a','b','d'],"subject1":[12,43,24,11,32,21,11],"subject2":[11,45,32,43,77,10,9]})
print(var)

var_new=var.groupby("name")
print(var_new)

for x,y in var_new:
    print(x)
    print(y)
    print()

print(var_new.get_group('c'))

print(var_new.min())

print(var_new.max())

print(var_new.mean())