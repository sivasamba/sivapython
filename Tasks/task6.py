EmpNam=input("Enter the employee Name:")
salry=float(input("Enter the employee salary:"))
desig=input("Enter employee designation:")
#bonus=int(input("Enter the employee bonus:"))
x="m"
y="a"
z="c"
if desig==x:
    salry=salry*120/100
    print("total salary=",salry)
elif desig==y:
    salry=salry*110/100
    print("total salry=",salry)
elif desig==z:
    salry=salry*105/100
    print("total salary=",salry)
else:
    print("please enter the designation within m/a/c")



