import os
import player


def visit_shop(player_name, player_hp, player_money, player_potions):
    """
    печатаем песронажа
    покупаем зелья тратим деньги
    варианты:
        Купить зелье(цена)
        обратно
    """

    input()

    is_shop = True
    while is_shop:
        player.show_player_stats(player_name, player_hp, player_money, player_potions)
        print("--Варианты")
        print("1 - купить зелье")
        print("2 - уйти")

        os.system("cls")

        answer = input("Введите номер варианта и нажмите ENTER! ")
        if answer == "1":
            if player_money >= 100:
                player_money -= 100
                player_potions += 1
                print(f"{player_name} купил зелье")
            else:
                print("У ВАС НЕТ ДЕНЕГ!!!")
        elif answer == "2":
            is_shop = False
