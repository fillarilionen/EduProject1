import random
def Cycle1(guess, riddle, counter) :
    while guess != riddle :
        if riddle > guess :
            print("Больше")
        else :
            print("Меньше")
        counter += 1
        guess = int(input())
    return counter

def Guess_the_number() :
    print("Число попыток дауна:", Cycle1(int(input()), random.randint(0,1000), 1))
Guess_the_number()

#Написать консольную программу игру “Угадай число”:
#1) Программа “загадывает” число от 0 до 1000 включительно.
#2) На ввод пользователя числа программа должна дать подсказку больше или меньше загаданное число.
#3) Если пользователь угадал число, программа выводит число попыток.
