############################################################################
#                _      _               _     ___     _   
#         __   _(_)_ __| |_ _   _  __ _| |   / _ \___| |_ 
#         \ \ / / | '__| __| | | |/ _` | |  / /_)/ _ \ __|
#          \ V /| | |  | |_| |_| | (_| | | / ___/  __/ |_ 
#           \_/ |_|_|   \__|\__,_|\__,_|_| \/    \___|\__|
#   ˚☽                                     
#  ｡       ☆                                           ☆         ☆
# ☆‌ ╭◜◝‌ ‌͡‌ ‌◜◝╮‌ ‌    ..... ‌҉‌ ‌        / `     ‌ ╭◜◝‌ ‌͡‌ ‌◜◝◜◝‌ ‌͡‌ ‌◜◝‌ ‌◜◝‌◜◝◜◝‌ ‌͡‌ ‌◜◝‌ ‌◜◝  
#  ‌ (‌ 。‌•‿•‌‌ ‌) ☆ (‌。•‿•‌‌ )  ‌      ‌<。‌•‿•‌。>  <   Like, Subscribe, Follow~! )          
#   ╰◟◞‌ ‌͜‌ ‌◟◞      ~~~~~ ☆    ‌҉‌ ‌  /, ,'\    ╰◟◞‌ ‌͜‌ ‌◟◞◟◞‌ ‌͜‌ ‌◟◞◟◞‌ ‌͜‌ ‌◟◞◟◞‌ ‌͜‌ ‌◟◞◟◞‌  

#            ☆                          ☆                 ☆            ☆
#               Virtual Star comes from a galaxy far, far away...                  
############################################################################


#                              Written by Sarah Bass
#                Check out my other games for Android, Fitbit, and more
#                           https://github.com/SarahBass


import random
pageNumber=1                              #
userInput=11
                              #
randnum=random.randint(2, 1299)           #
randnumber=random.randint(5, 120)         #
smallrandom=random.randint(0,10)          #
palindromenum=[5,6,7,9,11,12,14,15,       #
               17,18,19,21,28,35,36,      #
               37,42,63,73,74,84,85,      #
               94,101,111,119,126,131,    #
               185,202,303,404,409]       #
                                          #
gameLibrary = ["Roman Numeral",           #
               "Palindrome Pal",          #
               "Binary Beats",            #
               "Witch's Hex",             #
               "Power Ball",]             #
selector = 0                              #  
#-----------------------------------------#


###########################################################################################
###################MINI GAME LOGIC ########################################################
###########################################################################################
def intToRoman(num: int) -> str:
    M = ["", "M", "MM", "MMM"]
    C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    return M[num // 1000] + C[(num % 1000) // 100] + X[(num % 100) // 10] + I[num % 10]

def isPalindrome(self, x):
    if x > 0:
        temp = x
        rev_int_elements = []
        while temp > 0:
            digit = temp % 10
            rev_int_elements.append(digit)
            temp = temp // 10
        org_int_elements = rev_int_elements[::-1]
        return rev_int_elements == org_int_elements
    elif x == 0:
        return True
    else:
        return False

class Game:
    def __init__(self,name, answer, text, userAnswer):
        self.name = name
        self.answer = answer
        self.text = text
        self.userAnswer= userAnswer
game1 = Game("Roman Numeral", randnum, intToRoman(randnum),userInput)    
game2 = Game("Palindrome Pal", isPalindrome(isPalindrome,101), random.choice(palindromenum),isPalindrome(isPalindrome,(userInput*(random.choice(palindromenum))))) 
game3 = Game("Binary Beats", randnumber,bin(randnumber)[2:], userInput)
game4 = Game("Witch's Hex",randnumber,hex(randnumber)[2:],userInput)
game5 = Game("Power Ball",pow(2,smallrandom),smallrandom,userInput)


###########################################################################################
################### BUILD STAR CHARACTER ##################################################
###########################################################################################
class Star:
    def __init__(self, food, toy, hyg, sad, sick, happy, angry, edu, level ):
        self.food = food
        self.toy = toy
        self.hyg = hyg
        self.sad = sad
        self.sick = sick
        self.happy = happy  
        self.angry = angry  
        self.edu = edu
        self.level= level 
        
starpet = Star(0,0,0,0,0,5,0,0,0)

###########################################################################################
################### MANAGE BACKGROUND CHANGES #############################################
###########################################################################################


def BackgroundSwitch(level,sad, sick, angry,happy)-> str:
    match pageNumber:
        case 1:
            if level == 10:
                return "gameover"
            elif level == range(7,9):
                if sick > 0:
                    return "starsick"
                elif angry >0:
                    return "starangry"
                elif sad > 0:
                    return "starsad"
                else :
                    if happy > 8:
                        return "superhappystar"
                    elif happy == range(7,8):
                        return "happystar"
                    elif happy == range(5,6):
                        return "averagestar"
                    else:
                        return "sadstar"
            elif level ==range(3,6):
                if sick > 0:
                    return "nebulasick"
                elif angry >0:
                    return "nebulaangry"
                elif sad > 0:
                    return "nebulasad"
                else :
                    if happy > 8:
                        return "superhappynebula"
                    elif happy == range(7,8):
                        return "happynebula"
                    elif happy == range(5,6):
                        return "averagenebula"
                    else:
                        return "sadnebula"
            else :
                if sick > 0:
                    return "gassick"
                elif angry >0:
                    return "gasangry"
                elif sad > 0:
                    return "gassad"
                else :
                    if happy > 8:
                        return "superhappygas"
                    elif happy == range(7,8):
                        return "happygas"
                    elif happy == range(5,6):
                        return "averagegas"
                    else:
                        return "sadgas"
        case 2:
            return random.choice(gameLibrary)
        case 3:
            match selector:
                case 1:
                    return "funfood"
                case 2:
                    return "meteor"
                case 3:
                    return "shootingstar"
                case _:
                    return "Food"
        case 4:
            match selector:
                case 1:
                    return "animal"
                case 2:
                    return "spaceship"
                case 3:
                    return "satelite"
                case _:
                    return "toy"
        case 5:
            match selector:
                case 1:
                    return "bath"
                case 2:
                    return "brush"
                case 3:
                    return "medicine"
                case _:
                    return "hyg"
        case _:
            return "startscreen"

pagetype =(BackgroundSwitch(starpet.level,
                            starpet.sad,
                            starpet.sick,
                            starpet.angry,
                            starpet.happy))           
        

#-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=--=x=
#                        START OF GAME                            #  
#-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=--=x=


#-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=--=x=
#                         END OF GAME                            #
#-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=--=x=
print(starpet.food)
print(game1.answer)
print(game1.text)
print(game2.answer)
print(game2.text)
print(game2.userAnswer)
print(game3.text)
print(game3.answer)
print(game4.text)
print(game4.answer)
print(game5.text)
print(game5.answer)
print(starpet.happy)
print(pagetype)
