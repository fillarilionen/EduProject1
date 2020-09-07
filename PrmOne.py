#По имеющимся данным о пассажирах титаника “titanic.csv” с помощью библиотеки pandas необходимо найти самое популярное женское имя (считаются оба имени в двойных именах).
# 1. Посчитать количество женщин и мужчин
# 2. Посчитать количество пассажиров по каждому классу
import pandas as pd
import numpy as np
import collections
from collections import Counter
path = r"titanic.csv"
def cleaner_symbols(to_clean): #хавает str
    to_clean = to_clean.replace('(','')
    to_clean = to_clean.replace(')','')
    to_clean = to_clean.replace('Mrs.','')
    to_clean = to_clean.replace('Miss.','')
    to_clean = to_clean.split()
    del to_clean[0]
    return to_clean #высирает массив
def cleaner_dataframe(path) :
     titanic_list = pd.read_csv(path) #r чтобы в строке не учитывались спецсимволы
     titanic_list.drop(np.where(titanic_list['Sex'] == "male")[0], axis="rows", inplace=True) #where проходит по указанному массиву с условием и выдает T or F
     titanic_list.drop(["PassengerId" ,"Survived" ,"Pclass","Age","SibSp","Parch","Ticket","Fare","Cabin","Embarked", "Sex"],axis="columns", inplace=True )
     return titanic_list['Name']
# print(cleaner_dataframe(path))
# all_names = []
# for item in cleaner_dataframe(path) :
#     for item1 in cleaner_symbols(item) :
#         all_names.append(item1)
#print(Counter(all_names))



