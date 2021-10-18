f = open("E:\\python-lab\\Lab 9\\test.txt", "rt" , encoding='utf-8') 
lines = f.readlines()
d = dict()
for line in lines:
    for i in line:
        
        if i in d and i.isalpha() :
            d[i] += 1
        elif i.isalpha():
            d[i] = 1
f.close()
print(d)