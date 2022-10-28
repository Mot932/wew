import os
import game # импортируем файл game.


def show_menu():
    while True:
        os.system("cls")
        print("1 - Начать новую игру")
        print("0 - Выйти из игры")
        answer = input("Введите номер ответа и нажмите ENTER ")
        if answer == "1":
            game.start_new_game()
        elif answer == "0":
            print("Вы выходите из игры")
            break


show_menu()