List1 = [56, 78.84, "India"]
List1[0] = 100
print(type(List1))
print(List1)

b = list()
print(type(b))
print("b", b)

data = input()
print(list(data))


data = input("data: ")
print("type of data:", type(data))
list1 = data.split() # split() it is used to convert  a string into list.
print("list:", list1)
print("type of list:", type(list))

a =[10, 20, 30, 40]
print(a)
index = int(input("Enter  the index to print: "))

if index>len(a) or index < len(a):
    print("True")


chars = ['a', 'b', 'c', 'd']
print(chars)


