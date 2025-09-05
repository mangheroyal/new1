import pandas as pd
n=5
data={'Name':[1,2,3],'Phone':[4,5,6]}
#df=pd.DataFrame(data,index=['RA','RB','RC'])
index=range(0,9,1)
df=pd.DataFrame(data,index)
print('org')
print(df)


df.at['RC','C2']=65
print('new')
print(df)
