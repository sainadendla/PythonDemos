print('Larger Number Checker')
numA = int(input('Enter First Number: '))
numB = int(input('Enter Second Number: '))
numC =  int(input('Enter Third Number: '))
def main():
    if numA > numB and numA > numC:
        print('{} is the largest.'.format(numA))
    elif numB > numA and numB > numC:
        print('{} is the largest.'.format(numB))
    elif numC > numA and numC > numB:
        print('{} is the largest.'.format(numC))
    elif numA == numB == numC:
        print("All Numbers are Equal") 
    else:
        if numA == numB:
            print("First and Second Number are equally the largest")
        if numB == numC:
            print("Second and Third Number are equally the largest")
        if numA == numC:
            print("First and Third Number are equally the largest")

if __name__ == "__main__": main()
