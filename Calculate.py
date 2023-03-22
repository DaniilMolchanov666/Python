class Calculator:

    first_number = input('введите первое число: ')
    operation = input('введите знак: ')
    second_number = input('введите второе число: ')

    a = float(first_number)
    b = float(second_number)
    char = str(operation)

    if char == '+':
        print("{:0.3f}".format(a+b))
    elif char == '-':
        print("{:0.3f}".format(a-b))
    elif char == '*':
        print("{:0.3f}".format(a*b))
    elif char == '/':
        if b == 0:
            print('деление на ноль невозможно! введите снова числа')
        else:
            print("{:0.3f}".format(a/b))
    else:
        print('ошибка в формате ввода данных! попробуйте снова!')

