c=0
str= input('please enter any string: ')
s2= {'a','e','i','o','u'}
for i in str:
    if i in s2:
        c=c+1

print(c,"vowels are present")