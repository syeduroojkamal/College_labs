s1={1,5,2,7,3,4,12,14}
L= (s1)
s= set()
for i in s1:
    for j in s1:
        if i ==j:
            continue
        else:

            dif= abs(i-j)
        s.add(dif)
print(s)