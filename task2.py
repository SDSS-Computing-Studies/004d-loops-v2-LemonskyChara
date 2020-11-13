a = str(input("Enter a name: ")).strip()

nameList = ("Lebron","Kobe","Michale","Shaq","Dennis")

for i in nameList:
    if a == i:
        print("That name is on the list")
    else:
        print("That name is not on the list")
