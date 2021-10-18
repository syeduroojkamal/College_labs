from math import gcd
def get_gcd(a,b):
    print(gcd(a,b))
def get_lcm(a,b):
    print((a*b)/gcd(a,b))

n1 = int(input('enter first number'))
n2 = int(input('enter second number'))

get_gcd(n1,n2)
get_lcm(n1,n2)