print(5**6)
print("I'm a Boy")
print("Hello World".split('o'))
print("Intesert another string here: {}".format("INSERT ME!"))
print("Item one: {}, Item two: {}".format("Dog","Cat"))
print("Item one: {x}, Item two: {y}".format(y="Cat",x="Dog"))

#Lists
mylist = [1,2,3]
print(mylist)
mylist = ["string",1,2.0,True,[1,2,3]]
print(mylist)
print(mylist[:3])
print(mylist[::-1])
#Python list is mutatble
mylist[0]='mutate'
print(mylist)
mylist.append('new item')
print(mylist)
x = [34,66,77]
mylist.extend(x)
print(mylist)

#pop items from mylist
print(mylist.pop())
print(mylist)

#pop at index
print(mylist.pop(3))

#reverse
mylist.reverse()
print(mylist)

#sort
mylist.sort()
print(mylist)
print(mylist.count(True))


#dictionary - no order retained

x = {"key1":"value1","key2":"value2", "key3":{"keykey1":[2,"Grab Me",3]}}
print(x["key3"]["keykey1"][1].upper())
# add new key1
x["key4"]="burger"
print(x["key4"])

#Tuples
#tuples are immutable
t = (1,True,123)
print(t)

#sets
#unordered collections of unique elements
x = set()
x.add(2)
x.add(3)
x.add(0.1)
print(x)
