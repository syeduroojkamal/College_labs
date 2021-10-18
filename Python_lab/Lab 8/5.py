def perfect(n):
    t = [1]
    for i in range(2,n):
        if n % i == 0:
            t.append(i)
    
    if sum(t) == n:
        print(f'{n} is a perfect number😀')
    else:
        print(f'{n} is not a perfect number 🙁')
n = int(input('enter a no to check if it\'s perfect or not: '))
perfect(n)