L=[10,13,14,16,18,20]
n1=int(input("Enter first index"))
n2=int(input("Enter second index"))
temp=L[n1]
L[n1]=L[n2]
L[n2]=temp
print(L)