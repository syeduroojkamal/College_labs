f = open("E:\\python-lab\\Lab 9\\test.txt", "rt" , encoding='utf-8') 
s = open('second.txt' ,'w')
lines = f.readlines()
for line in lines:
    s.write(line)
f.close()
s.close()
s = open('second.txt' ,'r', encoding='utf-8')
lines = s.readlines()
for l in lines:
    print(l)