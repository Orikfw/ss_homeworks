number = str(input('Введіть чотирицифрове натуральне число:\n'))

#Знайти добуток цифр числа
r = 1
for i in number:
    r *= int(i)
print('Добуток цифр:', r)

#Записати число в реверсному порядку
print('Реверсний порядок:', ''.join(reversed(number)))

#Посортувати цифри
print('Відсортовані цифри:', sorted(number))