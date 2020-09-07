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
# - Найти контакт
# - Объединить контакты
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
def Main() :
    phone_number_list = pd.read_csv('PhoneBooks/Data.csv')
    phone_number_list = pd.phone_number_list(columns = ['Index', 'Name', 'Number', 'Position', 'Organisation'])
            print('Выберите действие\n', '1 - создать новый контакт\n', '2 - Просмотреть список контактов\n')
    if input() == 1 :
        NewContact(phone_number_list)




def NewContact(phone_number_list) :
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
    else:
        NewContact()
