first = (11, 22, 32, 55, 77, 44, 40, 55)
second = (32, 55, 55, 77, 11, 44, 40, 55)
t = []
for i in range(len(first)):
    if first[i] == second[i]:
        t.append(first[i])
print(t)