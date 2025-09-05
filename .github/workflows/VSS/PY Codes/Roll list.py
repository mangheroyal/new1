import numpy as np
import pandas as pd
    

#DATA INPUTTING
print('Welcome')
d=9
data={'Name':0,'Ph':1}
ind=range(0,d,1)
lis=pd.DataFrame(data,ind)
print(lis)
while True:
    #a=int(input("Enter your new entry.  "))
    b=int(input('Enter your Roll no.'))
    if b==9855:
        print(lis)
    elif ind==0:
        a=input("enter your name ")
        lis.at[b,'Name']= str(a)
        print('Your new record')
        print(lis)
    elif b==ind:
        print("Your old record ")
        print(lis)

    



#print(index)

