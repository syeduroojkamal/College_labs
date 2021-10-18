f = open("E:\\python-lab\\Lab 9\\test.txt", "rt" , encoding='utf-8') 
lines = f.readlines()
count = 0
for line in lines:
    if line.startswith('A'):
        pass
    else:
        count += 1
print(count)
f.close()