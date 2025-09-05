import random
while True:
    c=3
    r=random.randint(999,10000)
    print('.........................................................................')
    print(r)
    a=int(input('Enter your roll no. '))
    b=int(input('enter your OTP '))
    if b==r and c>-1:
                   print('Your attendace is marked...next please')
    else:
        while b<r or b>r:
              if b>r or b<r and c>-1:
                  c=c-1
                  print('wrong OTP  ')
                  print('Chances left ',c)
                  b=int(input('Try Another OTP  '))
              if c==0:
                  c=c-1
                  print('All chances are lost ')
                  print('.........................................................................')
              if b==r and c>-1:
                   print('Your attendace is marked...next please')
                   print('.........................................................................')
            
    










    





    






#Timer don't touch it............


#while True:
#    z=1
#    a=a+1
#    z=9999-a
#    if z>0:
#        print('your OTP validity timer          ',z)
#    if z==1:
#        r=98558
#        print('Your OTP is expired now :) ')              
    

    
