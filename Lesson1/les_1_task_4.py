"""
4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
и сколько между ними находится букв.
"""


a = ord(input('Введите первую букву: '))
b = ord(input('Введите вторую букву: '))

print(f'Буква {chr(a)} стоит на {a - 96} месте')
print(f'Буква {chr(b)} стоит на {b - 96} месте')
print(f'Между ними {abs(a - b) - 1} буква(ы)')
