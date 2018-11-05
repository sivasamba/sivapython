
numbers=[1,2,3,4,-3,-5,8,-7]
count1=0
count2=0
for x in numbers:
    if x==0:
       continue
    elif x>0:
        print(x,end=" ")
        count1+=1
    else:
         count2+=1
         print(x,end=" ")
print("\n  ")
print("no of +ve numbers is=",count1 )
print("no of -ve numbers is=",count2)

