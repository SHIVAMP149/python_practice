l1 = [11, 45, 8, 23, 14, 12, 78, 45, 89]

x = len(l1)//3
start = 0
end = x
for i in range(3):
    ind = slice(start,end)
    chunk = l1[ind]
    print("Chunk ",i,chunk)

    print("After reversing it : ",list(reversed(chunk)))

    start = end
    end += x


    
    