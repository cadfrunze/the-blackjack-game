

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
        random_useri = ["Scooter-Both", "Skoda-Both", "Palinka-Both", "Romania-Both", "Cadfrunze-Both", "U-Cluj-Both", "CFR-Both"]
        user2 = random.choice(random_useri)\
        
        userii["user1"] = user1
        userii["user2"] = user2
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
            if sum(user_1_int) == 21:
                os.system('cls')
                print(logo)
                print("Wow " + userii["user1"] + f" cartile tale sunt {user_1_str} si ai facut {sum(user_1_int)} Yuhuuuu!!!")
                scor_1 = scor_1 + 1
                game1 = False
                game2 = False
            elif sum(user_1_int) <= 20:
                os.system('cls')
                print(logo)
                print(userii["user1"] + f" cartile tale sunt {user_1_str}, si scorul tau este {sum(user_1_int)}")
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
                    print(userii["user1"] + f" cartile tale sunt {user_1_str} si scorul tau este {sum(user_1_int)}, ai renuntat sa mai joci!")
                    time.sleep(5)
                    game1 = False
                    input("Apasa enter pt a continua!")
                    print("Acum este randul " + userii["user2"] + " sa joace")
        elif sum(user_1_int) > 21:
            os.system('cls')
            print(logo)
            print("Din pacate " + userii["user1"] + f" cartile tale sunt {user_1_str} ai facut {sum(user_1_int)} punctaj si ai peste 21 de puncte")
            game1 = False
            input("Apasa enter pt a continua!")
            print("Acum este randul " + userii["user2"] + " sa joace")
    while game2:
        if user_2_int <= 17:
            os.system('cls')
            print(logo)
            print(userii["user2"] + f" cartile tale sunt {user_2_str} si scorul tau este {user_2_int}")
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
            print(userii["user2"] + f" cartile tale sunt {user_2_str} si scorul tau este {user_2_int}")
        elif user_2_int >= 18 and user_2_int <= 21:
            game2 = False
            if user_2_int == 21:
                os.system('cls')
                print(logo)
                print("Wow " + userii["user2"] + f" cartile tale sunt {user_2_str} si ai facut {user_2_int} Yuhuuuu!!!")
                scor_2 = scor_2 + 1
            else:
                os.system('cls')
                print(logo)
                print(userii["user2"] + f" cartile tale sunt {user_2_str} si scorul tau este {user_2_int}, si ai renuntat sa mai joci!")
                game2 = False

        elif user_2_int > 21:
            os.system('cls')
            print(logo)
            print("Din pacate " + userii["user2"] + f" cartile tale sunt {user_2_str} ai facut {user_2_int} punctaj si ai peste 21 de puncte")
            game2 = False
            
            
        

    
    
jocul(innregistrare, userii, scor_1, scor_2)

game0 = True

while game0:
    intrebare = input("Vrei sa joci in continujare?")
    if intrebare == "yes" or intrebare == "y":
        jocul(innregistrare=False, userii=userii, scor_1=scor_1, scor_2=scor_2)