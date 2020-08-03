def IsEven(num):
    if num%2==0:
        return True
    else:
        return False

n = int(input('Enter number : '))

if IsEven(n):
    print('The number you entered is Even.')
else:
    print('The number you entered is Odd.')
