a = int(input('Введите число '))
b = input('Введите действие (+,-,*,/) ')
c = int(input('Введите число '))

if b == '+':
    print(a + c)
elif b == '-':
    print(a - c)
elif b == '*':
    print(a * c)
elif b == '/':
    if c != 0:
        print(a / b)
    else:
        print('Делить на 0 нельзя')



