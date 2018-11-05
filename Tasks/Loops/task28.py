numbers=[1,2,3,4,5,6,7,8,9,10]
count1=0
count2=0
for x in numbers:
    if x==1:
        print("1 is not a prime number")
    elif (x%2) == 0:
        count1 += 1
    else:
        count2 += 1
print("\n  ")
print("no of non prime numbers is=",count1)
print("no of prime niumbers is=",count2)






