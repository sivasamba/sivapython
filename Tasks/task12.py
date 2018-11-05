#given two int values ,return the their sum. unless the two values are the  same ,then return double sum
def add(a,b):
    if a==b:
        return (a+b)*2
    elif a!=b:
        return a+b
a=int(input("Enetr the 1st num:"))
b=int(input("Enter the 2nd num:"))
print(add(a,b))