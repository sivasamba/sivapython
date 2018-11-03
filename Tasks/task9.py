def parrot_trouble(bol,t):
        if t<7:
            return True
        elif t>20:
            return True
        else:
            return False
bol=bool(input("Enter boolen:"))
t=int(input("Enter time in hours:"))
print(parrot_trouble(bol,t))
