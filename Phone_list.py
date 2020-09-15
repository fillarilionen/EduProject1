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
    while True:
        print('Проверьте правильность введенных данных ',Name,Number,Position,Organisation , '1 - Все правильно', '2 - Ввести заново') #переменная с текущим контактом
        if int(input()) == 1 :
            phone_number_list = phone_number_list.append({"Name": Name, "Number": Number, "Position": Position, "Organisation" : Organisation}, ignore_index=True)
            print(phone_number_list)
            break
        elif int(input()) == 2 :
            New_Contact(phone_number_list)
            break
        else:
            print('Введите правильное значение')
    phone_number_list.to_csv('PhoneBooks/Data.csv', index=False)

def Contact_editing(phone_number_list,contact_index) :
    print('Введите имя')
    Name = input()
    print('Введите номер')
    Number = input()
    print('Введите Должность') #сделать опционально
    Position = input()
    print('Введите Организацию') #сделать опционально
    Organisation = input()
    print('Проверьте правильность введенных данных',Name,Number,Position,Organisation , '1 - Все правильно', '2 - Ввести заново') #переменная с текущим контактом
    if int(input()) == 1 :
        phone_number_list.iloc[contact_index, :] = (Name,Number,Position,Organisation)
        phone_number_list.to_csv('PhoneBooks/Data.csv', index=False)
        print('Контакт успешно изменен!')
    elif int(input()) == 2:
        Contact_editing(phone_number_list,contact_index)

def Edit_and_delete(contact_index,phone_number_list) :
    print(phone_number_list.iloc[contact_index])
    print('1 - Редактировать\n', '2 - Удалить')
    if int(input()) == 1:
        Contact_editing(phone_number_list,contact_index)
        Main()
    elif int(input()) == 2:
        phone_number_list.drop([contact_index],axis="rows", inplace=True )
        phone_number_list.to_csv('PhoneBooks/Data.csv',index=False)
        Main()
    else:
        print('Введите правилную цифру')
        Edit_and_delete(contact_index,phone_number_list)

def Show_number_list(phone_number_list) :
    print(phone_number_list)
    print('Введите номер нужного контакта')
    Edit_and_delete(int(input()),phone_number_list)

def Main() :
    phone_number_list = pd.read_csv('PhoneBooks/Data.csv')
    print('Выберите действие\n', '0 - Выйти\n', '1 - создать новый контакт\n', '2 - Просмотреть список контактов\n')
    while True:
        zaebavshiy_menya_input = int(input())
        if zaebavshiy_menya_input == 0 :
            break
        elif zaebavshiy_menya_input == 1 :
            New_Contact(phone_number_list)
            Main()
        elif zaebavshiy_menya_input == 2 :
            Show_number_list(phone_number_list)
            Main()
        else:
            print('ведите правильное значение')
            Main()


Main()





