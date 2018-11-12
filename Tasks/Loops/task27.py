l1=[1,12,5,4,68,7,9,11]
l1.sort()
print(l1)
for x in range(1):
    if l1[-1]!=l1[-2]:
        print("first big number is:",l1[-1])
        print("the second big number is:",l1[-2])
    else:
        print("both are same:",l1[-1],l1[-2])
        print("the second big number is:",l1[-3])



