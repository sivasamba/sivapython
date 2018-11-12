name=input("Enter the name:")
l1=len(name)
print(l1)
n=0
for x in range(2,l1):
    for y in range(1,x):
        print(name[n],end="")
        n+=1
    print()