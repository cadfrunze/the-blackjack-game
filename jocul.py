
import random
import os
from art import logo
os.system('cls')


def jocul():
    """Jocul blackjack"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    intrebare1 = input("Doresti sa te joci?...Scrie \"yes\" or \"no\" >>> ")
    cards_user = []
    deal = random.choice(cards)
    cards_user.append(deal)
    deal = random.choice(cards)
    cards_user.append(deal)
    cards_dealer = random.choice(cards)
    joc1 = True
    joc2 = True
    while intrebare1 == "yes" or intrebare1 == "y" and joc1 == True:
        print(logo)
        print(f"Your cards: {cards_user}, current score {(sum(cards_user))}\nComputer's first card: {cards_dealer}")
        deal1 = input("Type 'y' to get another card, type 'n' to pass: ")
        os.system('cls')
        while deal1 == "y" or deal1 == "yes" and joc2 == True:
            os.system('cls')
            print(logo)
            deal = random.choice(cards)
            cards_user.append(deal)
            print(f"Your cards: {cards_user}, current score {(sum(cards_user))}\nComputer's first card: {cards_dealer}")
            if sum(cards_user) < 21:
                deal1 = input("Type 'y' to get another card, type 'n' to pass: ")
            elif sum(cards_user) == 21:
                print(f"Yuuuhuuu....{(sum(cards_user))}")
            elif sum(cards_user) > 21:
                print(f"{(sum(cards_user))}, ai peste 21")
                return (f"Ai facut {(sum(cards_user))}")

jocul()

