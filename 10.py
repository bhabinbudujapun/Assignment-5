#  python script to use IS operator to display if both
#  variables are the same object or not


data1 = 4
data2 = 4

result = data1 is data2

if result:
    print("Variables are the same object")
else:
    print("Variable are not the same object")
