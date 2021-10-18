f = open("E:\\python-lab\\Lab 9\\test.txt", "rt" , encoding='utf-8') 
lines = f.readlines()
list1 = list()
count = 0
for line in lines:
    list1.append(line)
    count += len(line.split(' '))
f.close()
n = len(list1)
while n > 0:
    print(list1[n-1])
    n -= 1
print('number of lines:',len(list1))
print('number of characters :',len(set(''.join(list1))))
print('number of words : ', count)