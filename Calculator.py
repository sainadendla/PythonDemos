import sys
print('Calculator')
type = str(input("Enter 1 for Addition, Enter 2 for Subtraction, Enter 3 for Multiplication, Enter 4 for Division: "))
if type == '1':
    print('You selected Addition')
    a = int(input('Enter Number One: '))
    b = int(input('Enter Number Two: '))
    answer = a + b 
    print(answer)
elif type == '2':
    print('You selected Subtraction')
    a = int(input('Enter Number One: '))
    b = int(input('Enter Number Two: '))
    answer = a - b
    print(answer)
elif type == '3':
    print('You selected Multiplication')
    a = int(input('Enter Number One: '))
    b = int(input('Enter Number Two: '))
    answer = a * b
    print(answer)
elif type == '4':
    print('You selected Division')
    a = int(input('Enter Number One: '))
    b = int(input('Enter Number Two: '))
    answer = a / b 
    print(answer)
else: 
    print('{} is not an option'.format(type))
    sys.exit()
