"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""

def menu():
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')
    choice = input('\nВыберите пункт меню: ')
    return choice
def addition(value_1, value_2):
    value_1 += value_2
    return value_1

account = 0
history = ''

while True:
    choice = menu()

    if choice == '1':
        print(f'\nНа вашем счету {account}')
        amount = int(input('Введите сумму для пополнения: '))
        account = addition(account, amount)
        print(f'На вашем счету после пополнения {account}\n')
        replemish = f'Пополнение на сумму {amount}. Остаток на счете: {account}\n'
        history = addition(history, replemish)
        # choice = menu()
    elif choice == '2':
        pay = input('Введите сумму товара для покупки: ')
        pay = round(float(pay), 2)
        if pay > account:
            print('Недостаточно средств. Пополните счет.')
            # choice = menu()
        else:
            pay = -pay
            account = addition(account,pay)
            payment = f'Покупка на сумму {pay}. Остаток на счете: {account}\n'
            print(payment)
            history = addition(history, payment)
            # choice = menu()
    elif choice == '3':
        print('\nИстория ваших покупок:')
        print(history)
        # choice = menu()
    elif choice == '4':
        print('Завершение работы')
        break
    else:
        print('Неверный пункт меню')
