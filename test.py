# dict_symb = {
#         "A": [1, 11],
#         "2": 2,
#         "3": 3,
#         "4": 4,
#         "5": 5,
#         "6": 6,
#         "7": 7,
#         "8": 8,
#         "9": 9,
#         "10": 10,
#         "J": 10,
#         "Q": 10,
#         "K": 10,

#     }
# test1 = dict_symb["A"][1] + 1
# print(test1)

# for a in range(0, 3):
#     print(a)
import time
import os
from art import logo
logo1 = ""
for afisare in range(len(logo)):
    logo1 = logo1 + logo[afisare]
    if afisare < 7:
        time.sleep(1)
    elif afisare > 7  and afisare < 18:
        time.sleep(0.3)
    os.system('cls')
    print(logo1)