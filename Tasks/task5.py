`name=input("enter customer name:")
slab=input("enter customer slab:")
a="i"
b="c"
c="r"
if slab==a:
    units=float(input("Enter the number of units used:"))
    units=units*5.25
    print("total amount is=",units)
elif slab==b:
    units = float(input("Enter the number of units used:"))
    units = units * 4.00
    print("total amount is=", units)
elif slab==c:
     units = float(input("Enter the number of units used:"))
     units = units * 3.08
     print("total amount is=", units)
else:
    print("pleas enter slab type is either i/c/r")