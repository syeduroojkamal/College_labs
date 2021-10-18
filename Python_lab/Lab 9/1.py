f = open("E:\\python-lab\\Lab 9\\test.txt", "rt" , encoding='utf-8') 
lines = f.readlines()
for line in lines:
    print(line)
f.close()