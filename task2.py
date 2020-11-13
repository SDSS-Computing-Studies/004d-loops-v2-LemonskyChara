nameList = ("Lebron","Kobe","Michale","Shaq","Dennis")

for a in nameList:
    a = str(input(""))
    if a in nameList:
        print("That name is on the list")
    elif a not in nameList:
        print("That name is not on the list")
