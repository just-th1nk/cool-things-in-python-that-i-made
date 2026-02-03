import random
def roll():
    print("Press ENTER to roll a dice! Type 'end' to end.") 
    x=input()
    dice=(random.randint(1, 6))
    if dice == 1 :
        print(""" -----
|     |
|  o  |
|     |
 -----""")
    if dice == 2:
        print(""" -----
|  o  |
|     |
|  o  |
 -----""")
    if dice == 3:
        print(""" -----
|o    |
|  o  |
|    o|
-----""")
    if dice == 4:
        print(""" -----
|o   o|
|     |
|o   o|
 -----""")
    if dice == 5:
        print(""" -----
|o   o|
|  o  |
|o   o|
 -----""")
    if dice == 6:
        print(""" -----
|o   o|
|o   o|
|o   o|
 -----""")
    if x != "end":
        roll()
    else:
        print("Thank you for playing.")
roll()