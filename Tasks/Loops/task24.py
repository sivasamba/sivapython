number=[int(input("enter any number:"))]
for x in number:
    if x==1:
        print("1 is not a prime number")
    elif (x%2)==0:\
        print(x,"given number is not prime")
    else:
        print(x,"given number is prime")
