l1 = [3,6,9,12,15,18,21]
l2 = [4,8,12,16,20,24,28]
l3 = []
l4 = []
for i in range(0,len(l1)):
    if i % 2 != 0:
        l3.append(l1[i])

for i in range(0,len(l2)):
    if i % 2 == 0:
        l4.append(l2[i])


print("LIST 1 : ",l1)
print("LIST 2 : ",l2)
print("NEW LIST AFTER ADDING : ",l3+l4)