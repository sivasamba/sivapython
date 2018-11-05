bol=bool(input("Enter bool:"))
hour=int(input("Enter current time:"))

def parrot_trouble(bol,hour):
    if bol==True:
        if hour>=6 or hour>=19:
            return True
    elif bol==True:
        if hour<=6 or hour<19:
            return False
    elif bol==False:
        if hour<0 and hour>0:
            return False




print(parrot_trouble(bol,hour))


