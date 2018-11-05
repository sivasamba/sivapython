def pos_neg(a,b,negative):
    if a>0 and b<0 :
        return True
    elif a<0 and b>0:
        return True
    elif a<0 and b<0:
        if negative==True:
            return True
        else:
            return False
    else:
        return False

a=int(input("Enter the a value:"))
b=int(input("enter the b value:"))
negative=bool(input("Enter boolean:"))
print(pos_neg(a,b,negative))

