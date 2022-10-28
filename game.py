import os
import shop
import player

def start_new_game():
    """
    Создает персонаж:
        Имя
        Здоровье
        деньги
        зелья
    """
    print("Запустили новую игру из файла")

    player_name = input("Введите имя игрока и нажмите ENTER ")
    if not player_name:
        player_name = "Александр"
    player_hp = 100
    player_money = 100
    player_potions = 1


    # запускаем главный цикл игры
    is_game = True
    while is_game:
        os.system("cls")

        player.show_player_stats(player_name, player_hp, player_money, player_potions)

        print("-- ситуация:")
        print(f"{player_name} приехал к камню.")
        print("-- варианты:")
        print("1 - поехать на битву")
        print("2 - поехать играть в кости")
        print("3 - поехать в лавку к ведьме")
        print("0 - выйти в главное меню")

        answer = input("Введите номер варианта и нажмите ENTER! ")
        if answer == "1":
            pass
        elif answer == "2":
            pass
        elif answer == "3":
            shop.visit_shop(player_name, player_hp, player_money, player_potions)
        elif answer == "0":
            is_game = False