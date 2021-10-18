L= [15,16,16,12,14,12,14]
L.sort()
print(L)
for i in L:
    if L.count(i)>1:
        L.remove(i)
        print(L)