#the parameter weekday is true if it is a weekday,and the parameter vacation is true if we are in tuble.
def sleep_in(weekday,vacation):
    if vacation or weekday!=True:
        return True
    elif vacation or weekday==True and vacation and weekday==False:
        return False
    else:
        return False


print(sleep_in(weekday=False,vacation=False))



