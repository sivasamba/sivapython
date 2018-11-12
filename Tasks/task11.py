def monkey_trouble(a_smile,b_smile):
    if a_smile and b_smile!=False:
        print("i am exected")
        return True
    elif b_smile or a_smile!=True:
        print("no i am executed")
        return True
    else:
        return False


print(monkey_trouble(a_smile=True,b_smile=False))











