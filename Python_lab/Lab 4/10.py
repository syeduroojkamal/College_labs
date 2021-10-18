import itertools

s = {1,2,3,4}
t = itertools.combinations(s,2)
for i in t:
    print(i)