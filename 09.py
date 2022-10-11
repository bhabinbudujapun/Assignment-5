#  python script to use NOT IN operator to display
#  the data not present in list

data = [11, 22, 33, 44, 55]

num = int(input("Enter number: "))

result = num not in data

print("List of data: ", end=' ')
for i in data:
    print(i, end=' ')

if result:
    print("\nYour number not in the list")
else:
    print("\nYour number in list")
