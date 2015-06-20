import sys
print("Prime Number Checker")
a = int(input('Enter a Number: '))
if a <= 1:
    print('Not Prime')
    sys.exit()
for i in range(2,a):
    if (a % i==0):
        print('Not Prime')
        break
else:
    print('Prime')
                