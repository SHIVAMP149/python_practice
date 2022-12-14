num = int(input("Enter the number of elements in the list: "))
list1 = []
for i in range(0,num):
    elements = int(input("Enter the numbere you want to enter: "))
    list1.append(elements)
print(list1)
list1.sort()
print(list1[-1])
