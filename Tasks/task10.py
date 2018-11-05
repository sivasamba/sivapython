tm=int(input("Enter the total marks:"))
if tm>360:
    print("'First Class'")
elif tm>=300 and tm<360:
    print("'Second Class'")
elif tm<300:
    print("'Third Class'")
