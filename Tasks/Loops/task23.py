#find the factorial of th given number
fact=int(input("Enter the factorial number:"))
if fact==0:
    print("0 does not have the factorial")
elif fact<0:
    print("-ve numbers does not hvae the factorial")
n=1
while fact>0:
    n=n*fact
    fact=fact-1
print("factorial of the given number is=",n)
 