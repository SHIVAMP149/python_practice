num = int(input("Enter the number of elements you want to enter: "))
list1 = []
for i in range(0,num):
    elements = input("Enter the elements: ")
    list1.append(int(elements))
print(list1)

if list1[0] == list1[-1]:
    print("True")
else:
    print("False")
