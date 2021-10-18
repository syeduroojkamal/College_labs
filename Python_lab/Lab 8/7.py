import string
def check_panagram(string1):
    if sorted(set(string1)) == sorted(set(string.ascii_lowercase)):
        print('Given string is panagram 😀')
    else:
        print('Givern string is not panagram 😑')
string1 = input('enter a string to check if it\'s panagram or not: ').replace(' ','')
check_panagram(string1.lower())