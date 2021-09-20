#Script:        List
#Author:        Kwesik
#Date:          20210919


# Experiments with lists
var1 = ['apple', 'banana', 'cherry', 'durian', 'eggplant','fuji', 'grape','honeydew', 'iceberg', 'jalapeno']
print(var1[3])
print(var1[5:9])

print('--- This is the end of the primary, and the start of the stretch goals ----')
mytuple = ("apple", "banana", "cherry")
myset = {"apple", "banana", "cherry"}
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

var1.append('kalamata')
mylist = var1.copy()
print(mylist)

print(mylist.count("grape"))

mylist.extend(mytuple)
print(mylist)

print(var1.index("eggplant"))

mylist.insert(1, "pineapple")
print(mylist)

var1.pop(6)
print(var1)

mylist.remove('cherry')
print(mylist)

mylist.reverse()
print(mylist)

var1.sort(reverse=False)
print(var1)

var1.clear()
print(var1)