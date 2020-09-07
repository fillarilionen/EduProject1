#По имеющимся данным о пассажирах титаника “titanic.csv” с помощью библиотеки pandas необходимо найти самое популярное женское имя (считаются оба имени в двойных именах).
# 1. Посчитать количество женщин и мужчин
# 2. Посчитать количество пассажиров по каждому классу
# 3. Создать функцию, которая будет принимать путь к Титаник.цсв и название колонки, причем название колонки вводится с клавы.
# Должна возвращать кол-во пассажиров сгруппированное по признакам. Учитывать ошибки ввода.
import pandas as pd

import numpy as np
import collections
from collections import Counter
import PrmOne
def passanger_counter(path, column_name) :
    titanic_list = pd.read_csv(path) #r чтобы в строке не учитывались спецсимволы
    return Counter(titanic_list[column_name])

titanic_list = pd.read_csv(r"titanic.csv")
print('Введите название колонки, которую хотите выебать')
print("Названия колонок:", titanic_list.columns.to_list())

while True :
    column_name = input()
    if column_name  in titanic_list.columns.to_list() :
        print(passanger_counter(PrmOne.path, column_name))
        break
    else :
        print('Уебок, введи нормальное название мать твою чих-пых')









