string1 = input('input first string: ')
string2 = input('input second string: ')

if len(string1) == len(string2):
    if set(string1) == set(string2):
        print('strings are equal')
    else:
        print('not equal')
else:
    print('string are not equal')