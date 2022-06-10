import sys
import random
import os
import time
from art import logo
os.system('cls')

innregistrare = True
userii = {
}
scor_1 = 0
scor_2 = 0
def jocul(innregistrare, userii, scor_1, scor_2):
    """Jocul blackjack"""
    
    if innregistrare == True:
        user1 = input("Username >>> ").capitalize()
        os.system('cls')
        print(f"Bun venit {user1} la jocul BLACK-JACK")
        random_useri = ["Scooter-Both", "Skoda-Both", "Palinka-Both", "Romania-Both", "Cadfrunze-Both", "U-Cluj-Both", "CFR-Both"]
        user2 = random.choice(random_useri)
        userii["user1"] = user1
        userii["user2"] = user2
        time.sleep(3)
        os.system("cls")
        print("Iata regulile jocului:")
        time.sleep(2)
        print("1. Cartile pentru joc sunt: [*'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', *'A', 'J', 'Q', 'K'].")
        time.sleep(2)
        print("2. Fiecare carte reprezinta un numar, (*cu exceptia cartii 'A' care poate fi 1 sau 11).\n   2.1 Astfel:\n       cartea 'J' este egala 10,\n       cartea 'Q' este egala 10,\n       cartea 'K' este egala tot cu 10.")
        time.sleep(2)
        print(f"3. {user1} primadata vei primi doua carti, si vor arata de exemplu asa: ['2', '7'].")
        time.sleep(2)
        print("4. Daca suma celor doua carti de exemplu: ['2', '7'] (2 + 7) este mai mica sau egala cu 10, ti se va genera automat urmatoarea carte.")
        time.sleep(2)
        print("5. Daca suma celor doua carti de exemplu: ['7', '3'] (7 + 3 = 10) este mai mica sau egala cu 10, atunci cartea 'A' este egala cu 11.\n   5.1. Pentru ca nu-i asa? 10 + 'A'(adica 11) = 21 :).\n   5.2. Iar daca suma numerelor din tabel de exemplu ['J', '5'] adica (15) depaseste suma de (11) atunci cartea 'A' este egala cu 1.) ")
        time.sleep(2)
        print("6. Intotdeauna cand ceri inca o carte dealerului ultima carte ti se va afisa in acest tabel [....].\n   6.1. De exemplu ['7', '3', 'A'] ultima carte fiind 'A'.\n   6.2. Cartea ti se va genera absolut aleatoriu (random) din tabelul de la pct1.")
        time.sleep(2)
        print("7. Scopul acestui joc este cine dintre playeri face 21, sau cine se apropie cel mai mult de numarul 21.\n   7.1. Cine face direct 21 din totalul cartilor automat va castiga partida!(fara a mai juca dealerul).\n   7.2. Tine minte! Dealerul este intotdeauna playerul calculator cel cu (\"-Both\").")
        time.sleep(2)
        print("\nDaca esti de acord cu regulile jocului scrie \"yes\" or \"y\" sau \"da\"")
        print("Daca nu esti de acord cu regulile jocului scrie \"no\" or \"n\" sau \"nu\"")
        acord = input("Raspunde aici >>> ")
        if acord == "no" or acord == "n" or acord == "nu":
            os.system('cls')
            print(f"Bine....tu ai vrut {user1}, jocul se va inchide!")
            time.sleep(3)
            sys.exit()
        incercare = 0
        while acord != "yes" and acord != "y" and acord != "da" and incercare <= 2:
            print("Nu am inteles. Reciteste regulile....")
            if acord == "no" or acord == "n" or acord == "nu":
                os.system('cls')
                print(f"Bine....tu ai vrut {user1}, jocul se va inchide!")
                time.sleep(3)
                sys.exit()
            elif incercare == 1:
                print("Ultima incercare!....")
            elif incercare == 2:
                os.system('cls')
                print(f"Bine....tu ai vrut {user1}, jocul se va inchide!")
                time.sleep(3)
                sys.exit()
            acord = input("Raspunde aici >>> ")
            incercare = incercare + 1
            os.system('cls')
            print("Al doilea player (calculator) este " + userii["user2"])   
    os.system('cls')
    print("Loading the game....")
    time.sleep(3)
    logo1 = ""
    for afisare in range(len(logo)):
        logo1 = logo1 + logo[afisare]
        if afisare < 7:
            time.sleep(1)
        elif afisare > 7  and afisare < 18:
            time.sleep(0.3)
        os.system('cls')
        print(logo1)
    time.sleep(3)
    symboluri = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    dict_symb = {
        "A": [1, 11],
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,

    }
    user_1_str = []
    user_1_int = []
    user_2_str = []
    user_2_int = 0
    game1 = True
    game2 = True
    
    for numar in range(0, 3):
        if numar == 0:
            user1_prov = random.choice(symboluri)
            for element in dict_symb:
                if user1_prov == element:
                    user_1_str.append(element)
            user1_prov = dict_symb[user1_prov]
            if user1_prov == dict_symb["A"]:
                if len(user_1_int) == 0:
                    user_1_int.append(dict_symb["A"][1])
                elif sum(user_1_int) <= 10:
                    user_1_int.append(dict_symb["A"][1])
                else:
                    user_1_int.append(dict_symb["A"][0])
            else:
                user_1_int.append(user1_prov)
        elif numar == 1:
            user2_prov = random.choice(symboluri)
            for element in dict_symb:
                if user2_prov == element:
                    user_2_str.append(element)
            user2_prov = dict_symb[user2_prov]
            if user2_prov == dict_symb["A"]:
                if user_2_int <= 10:
                    user_2_int = user_2_int + dict_symb["A"][1]
                else:
                    user_2_int = user_2_int + dict_symb["A"][0]
            else:
                user_2_int = user_2_int + user2_prov
        elif numar == 2:
            user1_prov = random.choice(symboluri)
            for element in dict_symb:
                if user1_prov == element:
                    user_1_str.append(element)
            user1_prov = dict_symb[user1_prov]
            if user1_prov == dict_symb["A"]:
                if len(user_1_int) == 0:
                    user_1_int.append(dict_symb["A"][1])
                elif sum(user_1_int) <= 10:
                    user_1_int.append(dict_symb["A"][1])
                else:
                    user_1_int.append(dict_symb["A"][0])
            else:
                user_1_int.append(user1_prov)
    while game1:
        if sum(user_1_int) <= 20 or sum(user_1_int) == 21:
            if sum(user_1_int) <= 10:
                os.system('cls')
                print(logo)
                print(userii["user1"] + f" cartile tale sunt {user_1_str}, si punctajul tau este {sum(user_1_int)}")
                print("Asteapta cartea!...")
                time.sleep(2)
                user1_prov = random.choice(symboluri)
                for element in dict_symb:
                    if user1_prov == element:
                        user_1_str.append(element)
                user1_prov = dict_symb[user1_prov]
                if user1_prov == dict_symb["A"]:
                    if len(user_1_int) == 0:
                        user_1_int.append(dict_symb["A"][1])
                    elif sum(user_1_int) <= 10:
                        user_1_int.append(dict_symb["A"][1])
                    else:
                        user_1_int.append(dict_symb["A"][0])
                else:
                    user_1_int.append(user1_prov)
            elif sum(user_1_int) == 21:
                os.system('cls')
                print(logo)
                print("Wow " + userii["user1"] + f" cartile tale sunt {user_1_str} si ai facut {sum(user_1_int)} Yuhuuuu!!!")
                scor_1 = scor_1 + 1
                game1 = False
                game2 = False
            elif sum(user_1_int) > 10 and sum(user_1_int)  <= 20:
                os.system('cls')
                print(logo)
                print(userii["user1"] + f" cartile tale sunt {user_1_str}, si punctajul tau este {sum(user_1_int)}")
                print("Mai doresti carte?...Scrie \"yes\" or \"y\" pentru \"da\" sau \"no\" or \"n\" pentru \"nu\"")
                intrebare1 = input("Raspuns >>> ")
                if intrebare1 == "yes" or intrebare1 == "y" or intrebare1 == "da":
                    print("Asteapta cartea!...")
                    time.sleep(2)
                    user1_prov = random.choice(symboluri)
                    for element in dict_symb:
                        if user1_prov == element:
                            user_1_str.append(element)
                    user1_prov = dict_symb[user1_prov]
                    if user1_prov == dict_symb["A"]:
                        if len(user_1_int) == 0:
                            user_1_int.append(dict_symb["A"][1])
                        elif sum(user_1_int) <= 10:
                            user_1_int.append(dict_symb["A"][1])
                        else:
                            user_1_int.append(dict_symb["A"][0])
                    else:
                        user_1_int.append(user1_prov)
                elif intrebare1 == "no" or intrebare1 == "n" or intrebare1 == "nu":
                    os.system('cls')
                    print(logo)
                    print("Deci " + userii["user1"] + f" cartile tale sunt {user_1_str} si punctajul tau este {sum(user_1_int)}, ai renuntat sa mai joci!")
                    print("Acum este randul " + userii["user2"] + " sa joace")
                    game1 = False
                    time.sleep(5)
                    x = input("Apasa enter pt a continua!")
                    while x != "":
                        x = input("Apasa enter pt a continua! (fara a scrie nimic in consola!)")
                elif intrebare1 != "no" and intrebare1 != "n" and intrebare1 != "nu" and intrebare1 != "yes" and intrebare1 != "y" and intrebare1 != "da":
                    os.system('cls')
                    print(logo)
                    print("Nu am inteles!...Te rog tasteaza corect din cerinte")
                    time.sleep(3)
                    continue
        elif sum(user_1_int) > 21:
            os.system('cls')
            print(logo)
            print("Din pacate " + userii["user1"] + f" cartile tale sunt {user_1_str} ai facut {sum(user_1_int)}, si ai peste 21 de puncte")
            game1 = False
            x = input("Apasa enter pt a continua!")
            while x != "":
                x = input("Apasa enter pt a continua! (fara a scrie nimic in consola!)")
            print("Acum este randul " + userii["user2"] + " sa joace")
    while game2:
        if user_2_int <= 17:
            os.system('cls')
            print(logo)
            print("Cartile lui " + userii["user2"] + f" sunt {user_2_str} si punctajul sau este {user_2_int}")
            print("Asteapta cartea!...")
            time.sleep(2)
            user2_prov = random.choice(symboluri)
            for element in dict_symb:
                if user2_prov == element:
                    user_2_str.append(element)
            user2_prov = dict_symb[user2_prov]
            if user2_prov == dict_symb["A"]:
                if user_2_int <= 10:
                    user_2_int = user_2_int + dict_symb["A"][1]
                else:
                    user_2_int = user_2_int + dict_symb["A"][0]
            else:
                user_2_int = user_2_int + user2_prov
            os.system('cls')
            print(logo)
            print("Cartile lui " + userii["user2"] + f" sunt {user_2_str} si punctajul sau este {user_2_int}")
        elif user_2_int >= 18 and user_2_int <= 21:
            game2 = False
            if user_2_int == 21:
                os.system('cls')
                print(logo)
                print("Wow " + userii["user2"] + f" cartile lui sunt {user_2_str} si a facut {user_2_int} Yuhuuuu!!!")
                scor_2 = scor_2 + 1
            else:
                os.system('cls')
                print(logo)
                print(userii["user2"] + f" cartile lui sunt {user_2_str} si punctajul sau este {user_2_int}, a renuntat sa mai joace!")
                game2 = False

        elif user_2_int > 21:
            os.system('cls')
            print(logo)
            print("Din pacate " + userii["user2"] + f" cartile lui sunt {user_2_str} a facut {user_2_int} punctajul lui este peste 21")
            game2 = False
    return {
        "user1": [user1, user_1_str, sum(user_1_int), scor_1],
        "user2": [user2, user_2_str, user_2_int, scor_2]
    }

userii = jocul(innregistrare, userii, scor_1, scor_2)
print(userii)    

    
    


# def castigator_remiza():
#     if sum(user_1_int) < 21 and user_2_int > 21:
#         scor_1 = scor_1 + 1
#         os.system('cls')
#         print(logo)
#         print(userii["user_1"]) + f" cartile tale sunt {user_1_str} si ai in total {sum(user_1_int)}"
#         time.sleep(2)
#         print(userii["user_2"]) + f" cartile tale sunt {user_2_str} si ai in total {user_2_int}"
#         time.sleep(2)
#         print("Aceasta runda a castigat " + userii["user_1"])
#         time.sleep(1)
#         print("Scorul vostru:")
#         time.sleep(1)
#         print(userii["user_1"] + f" : {scor_1}")
#         time.sleep(1)
#         print(userii["user_2"] + f" : {scor_2}")
#         time.sleep(1)
#         input("Apasa \"ENTER\" pentru a continua")
#     elif sum(user_1_int) > 21 and user_2_int < 21:
#             scor_2 = scor_2 + 1
#             os.system('cls')
#             print(logo)
#             print(userii["user_2"]) + f" cartile tale sunt {user_2_str} si ai in total {user_2_int}"
#             time.sleep(2)
#             print(userii["user_1"]) + f" cartile tale sunt {user_1_str} si ai in total {sum(user_1_int)}"
#             time.sleep(2)
#             print("Aceasta runda a castigat " + userii["user_2"])
#             time.sleep(1)
#             print("Scorul vostru:")
#             time.sleep(1)
#             print(userii["user_1"] + f" : {scor_1}")
#             time.sleep(1)
#             print(userii["user_2"] + f" : {scor_2}")
#             time.sleep(1)
#             input("Apasa \"ENTER\" pentru a continua")
#     elif sum(user_1_int) < 21 and user_2_int < 21:
#         if (21 - sum(user_1_int)) < (21 - user_2_int):
#             scor_1 = scor_1 + 1
#             os.system('cls')
#             print(logo)
#             print(userii["user_1"]) + f" cartile tale sunt {user_1_str} si ai in total {sum(user_1_int)}"
#             time.sleep(2)
#             print(userii["user_2"]) + f" cartile tale sunt {user_2_str} si ai in total {user_2_int}"
#             time.sleep(2)
#             print("Aceasta runda a castigat " + userii["user_1"])
#             time.sleep(1)
#             print("Scorul vostru:")
#             time.sleep(1)
#             print(userii["user_1"] + f" : {scor_1}")
#             time.sleep(1)
#             print(userii["user_2"] + f" : {scor_2}")
#             time.sleep(1)
#             input("Apasa \"ENTER\" pentru a continua")







game0 = True
# while game0:
#     intrebare = input("Vrei sa joci in continujare?")
#     if intrebare == "yes" or intrebare == "y":
#         jocul(innregistrare=False, userii=userii, scor_1=scor_1, scor_2=scor_2)