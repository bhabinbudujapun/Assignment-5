# python script to swap data of two variables

num1 = int(input("Enter first numbers: "))
num2 = int(input("Enter second numbers: "))

print("\nBefore Swap number:")
print("First Number: %d" % num1)
print("Second Number: %d" % num2)

num1, num2 = num2, num1

print("\nAfter Swap number:")
print("First Number: %d" % num1)
print("Second Number: %d" % num2)
