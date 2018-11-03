num=int(input("enter an integer number:"))
if num<=21:
    num=21-num
    print("difference is =",num)
else:
    if num>21:
        num=(num-21)*2
        print("difference over 21 is=",num)
