
for x in range(7,0,-2):
    for y in range(0,7-x):
        print(end=" ")
    for y in range(0,x):
        print("*",end=" ")
    print()

for x in range(1,8,2):
    for y in range(0,7-x):
        print(end=" ")
    for y in range(0,x):
        print("*",end=" ")
    print()

#* * * * * * *
 # * * * * *
  #  * * *
   #   *
    #  *
 #   * * *
#  * * * * *
#* * * * * * *

