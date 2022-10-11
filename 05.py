# python script which takes a three digit number
# from the user and displays only its first digit.

num = int(input("Enter the number: "))
new_num = num

while num > 9:
    new_num = num//10
    num //= 10

print("First digits: ", new_num)
