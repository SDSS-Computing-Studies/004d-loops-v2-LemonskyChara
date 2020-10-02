name =""

nameList = ("Lebron","Kobe","Michale","Shaq","Dennis")

for name in nameList:
    name = str(input("")).strip()
    if name in nameList:
        print("That name is in the list")
    else:
        print("That name is not in the list")
