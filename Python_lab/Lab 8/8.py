def sorted_string(s):
    t = s.split('-')
    t.sort()
    return '-'.join(t)

in_string = input('enter hyphen seperated string: ')
print(sorted_string(in_string))
