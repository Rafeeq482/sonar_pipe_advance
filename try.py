def createName(first, Last):
    first= first.capitalize()
    Last = Last.capitalize()
    return first + " " + Last

fullname = createName(input("enter first name: "), input("enter secound name: "))
print(fullname)