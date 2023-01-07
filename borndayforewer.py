"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""

# year = input('Ввведите год рождения А.С.Пушкина:')
# while year != '1799':
#     print("Не верно")
#     year = input('Введите год рождения А.С.Пушкина:')
#
# day = input('Введите день рождения Пушкин?')
# while day != '6':
#     print("Не верно")
#     day = input('В какой день июня родился Пушкин?')
# print('Верно')

def input_period(period):
    data = input(f'Ввведите {period} рождения А.С.Пушкина: ')
    return data
def check_period(period, value):
    if (period == 'год' and \
        value == '1799')    or \
        (period == 'месяц' and \
        value == '06') or \
        (period == 'день' and \
         value == '06'):

        print('Верно')
        return True

    else:
        print('Не верно')
        return False

periods = ['год', 'месяц', 'день']

for period in periods:
    data = input_period(period)
    while check_period(period, data) is  False:
        data = input_period(period)

print('Все верно')
