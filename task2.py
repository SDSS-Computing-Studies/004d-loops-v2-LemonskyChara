a =""

nameList = ("Lebron","Kobe","Michale","Shaq","Dennis")

for a in nameList:
    a = input("Enter a name: ")
    if a in nameList:
        print("That name is in the list")
    else:
        print("That name is not in the list")
