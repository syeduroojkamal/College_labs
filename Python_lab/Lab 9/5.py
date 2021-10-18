def count_a(lines):

    count = 0
    for line in lines:
    
        for i in line.split(' '):
        
            if i.endswith('a'):
                
                count += 1
    print(count)
f = open("E:\\python-lab\\Lab 9\\test.txt", "rt" , encoding='utf-8') 
lines = f.readlines()
count_a(lines)        
f.close()
