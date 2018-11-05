numbers=[1,2,3,4,5,10,20,40,7,8,9]
count1=0
count2=0
for x in numbers:
    if x%2==0:
        print(x,end=" ")
        count1+=1


    else:
         count2+=1
         print(x,end=" ")
print("\n  ")
print("no of even numbers is=",count1 )
print("no of odd numbers is=",count2)

