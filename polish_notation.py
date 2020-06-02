# num = (5 + 2)*3
# num = 5 + 2*3
# * + 5 2 3 => * 7 3 => 21
# + * 2 3 5 => + 6 5 => 11

possible_operators = ['+', '-', '*', '/']


def polish_notation(expression):
    operators = []
    for item in expression.split(' '):
        operators.append(item)
    assert operators[0] in possible_operators, 'Неизвестная операция.'
    assert len(operators) == 3, 'Неверное количество аргументов.'
    if operators[0] == '+':
        try:
            result = int(operators[1]) + int(operators[2])
            print(result)
        except ValueError as e2:
            print(f'Строки складывать нельзя. Текст исключения: {e2}')
    elif operators[0] == '-':
        try:
            result = int(operators[1]) - int(operators[2])
            print(result)
        except ValueError as e2:
            print(f'Строки вычитать нельзя. Текст исключения: {e2}')
    elif operators[0] == '*':
        try:
            result = int(operators[1]) * int(operators[2])
            print(result)
        except ValueError as e2:
            print(f'Строки умножать нельзя. Текст исключения: {e2}')
    elif operators[0] == '/':
        try:
            result = int(operators[1]) / int(operators[2])
            print(result)
        except ZeroDivisionError as e1:
            print(f'На ноль делить нельзя. Текст исключения: {e1}')
        except ValueError as e2:
            print(f'Строки делить нельзя. Текст исключения: {e2}')


expression = input()
polish_notation(expression)