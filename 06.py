# python script which takes a three digit number
# from the user and displays only its middle digit.

num = int(input("Enter the number: "))

num1 = num
num1 //= 10
num1 %= 10

print("Your number: ", num)
print("Middle number: ", num1)
