#wap to convert a given list of integer and a tuple of integer in a list of string ussing map().
a = [10, 20, 30]
b = (40, 50, 60)

list1 = list(map(lambda x: str(x), a))
list2 = list(map(lambda x: str(x), b))

print(list1)
print(list2)
