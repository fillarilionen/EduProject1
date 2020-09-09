# реализовать телефонный справочник.
# Поля:
# - Имя
# - Номер
# - Компания
# - Должность
# Функции:
# - Добавить новый контакт
# - Удалить контакт
# - Редактировать контакт
# - Просмотреть список контактов

# Реализовать проверку введенного номера телефона(может быть введен в формате +79681234567, 8(968)1234567), 8-968-595-31) и приводить номер при записи всегда к формату 8(968)595-31-78.
# Номера сохраняются в csv-файл.
# вывод в консоль.
# В процессе написания использовать git
import pandas as pd
import numpy as np
import collections

from collections import Counter
# Файл, в котором хранятся данные(по умолчанию Data.csv) лежит в корне проекта, в папке PhoneBooks.
# Пользователь при желании может создать другой файл. Реализовать возможность переключения между файлами. Мердж файлов(все, список выбранных).
# Если файл Data.csv не найден, предложить другие файлы на выбор, если их нет то создать новый(Data.csv).
def New_Contact(phone_number_list) :
    print('Введите имя')
    Name = input()
    print('Введите номер')
    Number = input()
    print('Введите Должность') #сделать опционально
    Position = input()
    print('Введите Организацию') #сделать опционально
    Organisation = input()
    print('Проверьте правильность введенных данных',Name,Number,Position,Organisation , '1 - Все правильно', 'Ввести заново') #переменная с текущим контактом
    if input() == 1 :
        phone_number_list = phone_number_list.append({'Name': Name, 'Number': Number, 'Position': Position, 'Organisation' : Organisation}, ignore_index=True)

        return()

def Contact_editing(phone_number_list) :
    print('Введите имя')
    Name = input()
    print('Введите номер')
    Number = input()
    print('Введите Должность') #сделать опционально
    Position = input()
    print('Введите Организацию') #сделать опционально
    Organisation = input()
    print('Проверьте правильность введенных данных',Name,Number,Position,Organisation , '1 - Все правильно', 'Ввести заново') #переменная с текущим контактом
    if input() == 1 :
        phone_number_list = phone_number_list.append({'Name': Name, 'Number': Number, 'Position': Position, 'Organisation' : Organisation}, ignore_index=True)

        return()

def Show_number_list_sub(number_index) :
    print(phone_number_list[number_index])
    print('1 - Редактировать\n', '2 - Удалить')
    if input() == 1
        Contact_editing()
    if input == 2
        phone_number_list.drop([],axis="columns", inplace=True )
    else:
        print('Введите правилную цифру')
        Show_number_list_sub()



def Show_number_list() :
    print(phone_number list)
    print('Введите номер нужного контакта')
    number_index = input()
    Show_number_list_sub(number_index)




def Main() :
    phone_number_list = pd.read_csv('PhoneBooks/Data.csv')
    phone_number_list = pd.phone_number_list(columns = ['Index', 'Name', 'Number', 'Position', 'Organisation'])
    print('Выберите действие\n', '1 - создать новый контакт\n', '2 - Просмотреть список контактов\n')
    while True
        if input() == 1 :
            New_Contact(phone_number_list)
        if input() == 2 :
            Show_number_list()
        if

Main()





