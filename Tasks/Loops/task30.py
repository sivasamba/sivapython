fourdigit=int(input("enter any four digit number"))
sum=0
for x in fourdigit:
    if x>0:
        dig=fourdigit/10
        sum=sum+dig
        fourdigit=fourdigit//10
 print("sum four digits=",dig)





