from math import factorial
 
def print_pascal(n):
    for i in range(n):
        for j in range(n-i+1):
 
        
            print(end=" ")
 
        for j in range(i+1):
 
        
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
 
    
        print()
n = int(input('Enter no. of rows: '))
print_pascal(n)

