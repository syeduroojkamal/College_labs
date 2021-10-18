num1 = float(input("Enter a number: "))
num2 = float(input("Another one : "))
num3 = float(input("Another one : "))
if (num1 > num2) and (num1 > num3):
    largest_num = num1
elif (num2 > num1) and (num2 > num3):
    largest_num = num2
else:
    largest_num = num3
print("The largest of the 3 numbers is : ", largest_num)