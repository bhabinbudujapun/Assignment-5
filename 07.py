# python script which takes a three digit number
# from the user and displays only its last digit.

num = int(input("Enter the number: "))

print("Your number: ", num)
num %= 10

print("Last digits of your number: ", num)
