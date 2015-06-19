print('Prime Number Printer')
a = int(input('Enter a Number: '))
for x in range(1, a +1):
    for i in range(2,x):
        if (x % i==0):
            break
    else:
       print(x)
                
            