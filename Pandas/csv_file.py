import pandas as pd
dis={'a':[1,2,3,4],'b':[2,3,4,5],'c':[3,5,2,1]}
d=pd.DataFrame(dis)
print(d)

d.to_csv("test_new.csv",index=False)