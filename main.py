RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
GREEN = '\u001b[48;5;34m'
YELLOW = '\u001b[48;5;11m'
BLACK = '\u001b[48;5;16m'
END = '\u001b[0m'

print('Флаг: Швейцария')

for i in range(7):
    if i == 1 or i == 2 or i == 4 or i == 5:
        print(f'{RED}{"  " * 7}{WHITE}{"  " * 3}{RED}{" " * 14}{END}')
    elif i == 3:
        print(f'{RED}{"  " * 4}{WHITE}{"  " * 9}{RED}{" " * 8}{END}')
        print(f'{RED}{"  " * 4}{WHITE}{"  " * 9}{RED}{" " * 8}{END}')
    else:
        print(f'{RED}{" " * 34}{END}')

print('\n', 'Узор: j')

# for i in range(7):
#     if i == 2 or i == 3 or i == 4:
#         print(f'{END}{' ' * 0}{GREEN}{' ' * 3}{END}{' ' * 15}{GREEN}{' ' * 3}{END}{' ' * 0}{END}{' ' * 0}{GREEN}{' ' * 0}{END}{' ' * 15}{GREEN}{' ' * 3}{END}')
#     if i == 0 or i == 6:
#         print(f'{END}{' ' * 6}{GREEN}{' ' * 9}{END}{' ' * 6}{END}{' ' * 3}{GREEN}{' ' * 9}{END}')
#     if i == 1 or i == 5:
#         print(f'{END}{' ' * 3}{GREEN}{' ' * 3}{END}{' ' * 9}{GREEN}{' ' * 3}{END}{' ' * 3}{END}{' ' * 0}{GREEN}{' ' * 3}{END}{' ' * 9}{GREEN}{' ' * 3}{END}')
# print()

for i in range(9):
    if i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
        print(
            f'{END}{' ' * 0}{GREEN}{' ' * 3}{END}{' ' * 21}{GREEN}{' ' * 3}{END}{' ' * 0}{END}{' ' * 0}{GREEN}{' ' * 0}{END}{' ' * 21}{GREEN}{' ' * 3}{END}')
    if i == 0 or i == 8:
        print(f'{END}{' ' * 6}{GREEN}{' ' * 15}{END}{' ' * 6}{END}{' ' * 3}{GREEN}{' ' * 15}{END}')
    if i == 1 or i == 7:
        print(
            f'{END}{' ' * 3}{GREEN}{' ' * 3}{END}{' ' * 15}{GREEN}{' ' * 3}{END}{' ' * 3}{END}{' ' * 0}{GREEN}{' ' * 3}{END}{' ' * 15}{GREEN}{' ' * 3}{END}')

print('\n Функция: y = x/3')

for i in range(15, -1, -1):
    if i == 15:
        print(f'5 |{WHITE}{' ' * ((15 // 3) * 2 + 22)}{RED}{' ' * 3}{END}')
    if i == 12:
        print(f'4 |{WHITE}{' ' * ((12 // 3) * 2 + 16)}{RED}{' ' * 8}{WHITE}{' ' * (27 - (int(12 // 3)) * 6)}{END}')
    if i == 9:
        print(f'3 |{WHITE}{' ' * ((9 // 3) * 2 + 10)}{RED}{' ' * 8}{WHITE}{' ' * (29 - (int(9 // 3)) * 6)}{END}')
    if i == 6:
        print(f'2 |{WHITE}{' ' * ((6 // 3) * 2 + 6)}{RED}{' ' * 6}{WHITE}{' ' * (31 - (int(6 // 3)) * 6)}{END}')
    if i == 3:
        print(f'1 |{WHITE}{' ' * ((3 // 3) * 2 + 2)}{RED}{' ' * 6}{WHITE}{' ' * (31 - (int(3 // 3)) * 6)}{END}')
    if i == 0:
        print(f'0 |{WHITE}{' ' * (0 // 3)}{RED}{' ' * 4}{WHITE}{' ' * (31 - (int(0 // 3)) * 2)}{END}')
print(f'{"   "}{"-" * 35}')
print(f'{"   "}{"1 2 3 4 5 6 7 8 9 10 11 12 13 14 15"}\n')


print('\nУсловие: числа от -3 до 3 и другие числа')

data = [float(i) for i in open('sequence.txt')]
first_group = []
second_group = []

for i in data:
    if -3 < i < 3:
        first_group.append(i)
    else:
        second_group.append(i)

print(f'числа от -3 до 3 {GREEN}{' ' * int((len(first_group) / len(data)) * 100)}{END}{round((len(first_group) / len(data)) * 100, 2)} %')
print(f'остальные числа  {YELLOW}{' ' * int((len(second_group) / len(data)) * 100)}{END}{round((len(second_group) / len(data)) * 100, 2)} %')
