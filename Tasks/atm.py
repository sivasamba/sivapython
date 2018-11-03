#1.check pin number
#2.check the input number
#3.check max withdraw
#4.check the balance
#5.show the available balnce

print("welocme to sbi atm")
print("please insert the atm card")
pin=input("enter valid pin number:")
Balance=20000
if pin=="9999":
   amount=int(input("enter the input amount:"))
   if(amount%100)==0:
       if amount<=10000:
           print("valid amount")
           Balance=20000-amount
           print("reaming balance is =",Balance)
           if Balance!=0:
               print("existed from the transaction")


       else:
           print("please enter valid amount")
   else:
       print("amount is not valid")
else:
    print("please enter the valid pin")