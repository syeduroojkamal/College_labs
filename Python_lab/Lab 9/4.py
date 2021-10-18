def display_words(lines):

    for line in lines:
    
        for i in line.split(' '):
        
            if len(i) <= 4:
                print(i)


f = open("E:\\python-lab\\Lab 9\\test.txt", "rt" , encoding='utf-8') 
lines = f.readlines()

display_words(lines)
f.close()
