s=input("enter the string : ")
a,b=s.split(" ")
new_a = b[:2] + a[2:]
new_b = a[:2] + b[2:]
print(new_a,new_b)
