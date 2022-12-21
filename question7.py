set1 = {27, 43, 34}
set2 = {34, 93, 22, 27, 43, 53, 48}

if set2.issubset(set1):
    
    set1.clear()
    print(set1)  

if set1.issubset(set2):
    set2.clear()
    print(set2)


if set2.issuperset(set1):

    set1.clear()
    print(set1)

if set1.issuperset(set2):
    set2.clear()
    print(set2)