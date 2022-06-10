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
def jocul(innregistrare, userii, scor_1, scor_2,scorul):
    """The black-jack game!"""
    # Innregistrare useri (prima data cand ruleaza jocul)
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
        print("2. Fiecare carte reprezinta un numar, (*cu exceptia cartii 'A' care poate fi 1 sau 11).\n   2.1. Astfel:\n       2.1.1 Cartea 'J' este egala 10,\n       2.1.2 Cartea 'Q' este egala 10,\n       2.1.3 Cartea 'K' este egala tot cu 10.")
        time.sleep(2)
        print(f"3. {user1} primadata vei primi doua carti, si vor arata de exemplu asa: ['2', '7'].")
        time.sleep(2)
        print("4. Daca suma celor doua carti de exemplu: ['2', '7'] (2 + 7) este mai mica sau egala cu 10, ti se va genera automat urmatoarea carte.")
        time.sleep(2)
        print("5. Daca suma celor doua carti de exemplu: ['7', '3'] (7 + 3 = 10) este mai mica sau egala cu 10, atunci cartea 'A' este egala cu 11.\n   5.1. Pentru ca nu-i asa? 10 + 'A'(adica 11) = 21 :).\n   5.2. Iar daca suma numerelor din tabel de exemplu ['J', '5'] adica (15) depaseste suma de (11) atunci cartea 'A' este egala cu 1.) ")
        time.sleep(2)
        print("6. Intotdeauna cand ceri inca o carte dealerului ultima carte ti se va afisa in acest tabel [....].\n   6.1. De exemplu ['7', '3', 'A'] ultima carte fiind 'A'.\n   6.2. Cartea ti se va genera absolut aleatoriu (random) din tabelul de la pct 1.")
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
        time.sleep(2)
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
    # Rularea jocului
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
    # Rulare joc player 1
    while game1:
        if scorul == True:
            print("Pana acum scorul este:")
            print(rezultat["user1"][0] + ": " + str(rezultat["user1"][3]) + ".")
            print(rezultat["user2"][0] + ": " + str(rezultat["user2"][3]) + ".")

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
    # Rulare joc player 2
    while game2:
        if scorul == True:
            print("Pana acum scorul este:")
            print(rezultat["user1"][0] + ": " + str(rezultat["user1"][3]) + ".")
            print(rezultat["user2"][0] + ": " + str(rezultat["user2"][3]) + ".")

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
                x = input("Apasa enter pt a continua!")
                while x != "":
                    x = input("Apasa enter pt a continua! (fara a scrie nimic in consola!)")
            else:
                os.system('cls')
                print(logo)
                print(userii["user2"] + f" cartile lui sunt {user_2_str} si punctajul sau este {user_2_int}, a renuntat sa mai joace!")
                x = input("Apasa enter pt a continua!")
                while x != "":
                    x = input("Apasa enter pt a continua! (fara a scrie nimic in consola!)")

        elif user_2_int > 21:
            os.system('cls')
            print(logo)
            print("Din pacate " + userii["user2"] + f" cartile lui sunt {user_2_str} a facut {user_2_int} punctajul lui este peste 21")
            game2 = False
            x = input("Apasa enter pt a continua!")
            while x != "":
                x = input("Apasa enter pt a continua! (fara a scrie nimic in consola!)")
    # Rezultatele
    return {
        "user1": [user1, user_1_str, sum(user_1_int), scor_1],
        "user2": [user2, user_2_str, user_2_int, scor_2]
    }

primul_joc = True
if primul_joc == True:
    rezultat = jocul(innregistrare, userii, scor_1, scor_2, scorul=False)

# Calculare, afisarea scorului
os.system('cls')
print(logo)
print("Cartile lui " + rezultat["user1"][0] + " sunt " + str(rezultat["user1"][1]) + " si a facut " + str(rezultat["user1"][2]) + ".")
time.sleep(2)
print("Cartile lui " + rezultat["user2"][0] + " sunt " + str(rezultat["user2"][1]) + " si a facut " + str(rezultat["user2"][2]) + ".")
time.sleep(2)
if rezultat["user1"][2] == rezultat["user2"][2]:
    print("Remiza!")
elif rezultat["user1"][2] == 21:
    print("Felicitari " + rezultat["user1"][0] + " ai castigat partida!.")
    rezultat["user1"][3] = rezultat["user1"][3] + 1
elif rezultat["user2"][2] == 21:
    print("Felicitari " + rezultat["user2"][0] + " ai castigat partida!")
    rezultat["user2"][3] = rezultat["user2"][3] + 1
elif rezultat["user1"][2] < 21 and rezultat["user2"][2] > 21:
    print("Felicitari " + rezultat["user1"][0] + " ai castigat partida!.")
    rezultat["user1"][3] = rezultat["user1"][3] + 1
elif rezultat["user2"][2] < 21 and rezultat["user1"][2] > 21:
    print("Felicitari " + rezultat["user2"][0] + " ai castigat partida!")
    rezultat["user2"][3] = rezultat["user2"][3] + 1
elif rezultat["user1"][2] < 21 and rezultat["user2"][2] < 21:
    if (21 - rezultat["user1"][2]) < (21 - rezultat["user2"][2]):
        print("Felicitari " + rezultat["user1"][0] + " ai castigat partida!.")
        rezultat["user1"][3] = rezultat["user1"][3] + 1
    else:
        print("Felicitari " + rezultat["user2"][0] + " ai castigat partida!")
        rezultat["user2"][3] = rezultat["user2"][3] + 1
elif rezultat["user1"][2] > 21 and rezultat["user2"][2] > 21:
    if (rezultat["user1"][2] - 21) < (rezultat["user2"][2] - 21):
        print("Felicitari " + rezultat["user1"][0] + " ai castigat partida!.")
        rezultat["user1"][3] = rezultat["user1"][3] + 1
    else:
        print("Felicitari " + rezultat["user2"][0] + " ai castigat partida!")
        rezultat["user2"][3] = rezultat["user2"][3] + 1

scorul = True
if scorul == True:
    print("Pana acum scorul este:")
    print(rezultat["user1"][0] + ": " + str(rezultat["user1"][3]))
    print(rezultat["user2"][0] + ": " + str(rezultat["user2"][3]))
input("enter")
os.system('cls')
game0 = True
while game0:
    print("1. Vrei sa joci in continuare?. Scrie \"yes\" or \"y\" sau \"da\".")
    print("2. Vrei sa iesi din joc?. Scrie \"no\" or \"n\" sau \"nu\".")
    intrebare0 = input("Raspunde aici >>> ")
    while intrebare0 != "yes" and intrebare0 != "y" and intrebare0 != "da" and intrebare0 != "YES" and intrebare0 != "Y" and intrebare0 != "DA" and intrebare0 != "no" and intrebare0 != "n" and intrebare0 != "nu" and intrebare0 != "NO" and intrebare0 != "N" and intrebare0 != "NU":
        os.system('cls')
        print("Nu am inteles....te rog reciteste ce am scris mai sus. Multumesc.")
        intrebare0 = input("Raspunde aici >>> ")
    if intrebare0 == "yes" or intrebare0 == "y" or intrebare0 == "da" or intrebare0 == "YES" or intrebare0 == "Y" or intrebare0 == "DA":
        os.system('cls')
        print("1. Scrie \"1\" daca doresti sa joci fara a reseta scorul si playerii innregistrati.")
        print("2. Scrie \"2\" daca doresti sa stergi playerii si scorul innregistrat.")
        print("3. Scrie \"3\" daca doresti doar scorul sa fie resetat.")
        intrebare1 = input("Raspunde aici >>> ")
        while intrebare1 != "1" and intrebare1 != "2" and intrebare1 != "3":
            os.system('cls')
            print("1. Scrie \"1\" daca doresti sa joci fara a reseta scorul si playerii innregistrati.")
            print("2. Scrie \"2\" daca doresti sa stergi playerii si scorul innregistrat.")
            print("3. Scrie \"3\" daca doresti doar scorul sa fie resetat.")
            print("Nu am inteles. Te rog reciteste ce am scris mai sus. Multumesc.")
            intrebare1 = input("Raspunde aici >>> ")
        if intrebare1 == "1":
            primul_joc = False
            rezultat = jocul(innregistrare=False, userii=rezultat, scor_1=rezultat["user1"][2], scor_2=rezultat["user2"][2], scorul=True)
        elif intrebare1 == "2":
            primul_joc = False
            innregistrare = True
            userii = {}
            scor_1 = 0
            scor_2 = 0
            rezultat = jocul(innregistrare, userii, scor_1, scor_2, scorul=True)
        elif intrebare1 == "3":
            primul_joc = False
            innregistrare = False
            scor_1 = 0
            scor_2 = 0
            rezultat = jocul(innregistrare, userii, scor_1, scor_2, scorul=True)
    elif intrebare0 == "no" or intrebare0 == "n" or intrebare0 == "nu" or intrebare0 == "NO" or intrebare0 == "N" or intrebare0 == "NU":
        os.system('cls')
        print("Jocul s-a inchis!")
        time.sleep(2)
    