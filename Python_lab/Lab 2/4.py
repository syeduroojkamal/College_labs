L= [2,3,2,4,3,3]
print('list before deletion',L)
n,o = input('enter value to remove and the occurance ').split()
c = 0
le = len(L)
for i in range(le):
    
    if L[i] == int(n):
        c += 1
        if c == int(o):
            L.pop(i)
            break
    
print(L)
