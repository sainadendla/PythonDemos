print('Pyramid Printer2')
a = int(input('Enter a Number: '))
b = '1'
c = 1
d = a 
e = 2
while c <= a:
    print(d*' ' + b)
    b += " " + str(e)
    c += 1
    d -= 1
    e += 1