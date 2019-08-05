first = input('Введіть першу змінну:\n')
second = input('Введіть другу змінну:\n')

print(f'До заміни: \nПерша змінна: {first}, Друга змінна: {second}')

first, second = second, first

print(f'Після заміни: \nПерша змінна: {first}, Друга змінна: {second}')