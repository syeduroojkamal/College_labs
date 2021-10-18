# warning : not working as intendend 
def showEmployee(name , salary = 9000):
    print(name,salary)
name = input('Enter the name: ')
salary = int(input('enter salary'))
showEmployee(name)