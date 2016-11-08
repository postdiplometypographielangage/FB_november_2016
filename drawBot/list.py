myList = ["hello", "second", "third"]

print myList
myList.append("he Here Im!")
print myList

print myList[0]
print myList[1]
print myList[2]
print myList[3]

myList.insert(0, "Actually Im the First")
print myList

myList.remove("third")
print myList
# myList.remove("im not in there")

for something in myList:
    print something
    
print "Im done"


