def count_case(a):
    count_u = 0
    count_l = 0
    for i in a:
        if i.isupper():
            count_u += 1
        elif i.islower():
            count_l += 1
    print('uppercase',count_u)

    print('lowercase', count_l)

string = input('Enter a string: ')
count_case(string)