set1 = {23, 42, 65, 57, 78, 83, 29}
set2 = {57, 83, 29, 67, 73, 43, 48}

print("SET 1 IS : ",set1)
print("SET 2 IS : ",set2)

common = set1.intersection(set2)
print("INTERSECTION ARE : ",common)

diff = set1 - set2

print("SET AFTER REMOVING COMMON ELEMENTS FROM SET1 : ",diff)
