import random
pagetype = "sadgas"
userInput=11
randnum=random.randint(2, 1299)
randnumber=random.randint(5, 120)
smallrandom=random.randint(0,10)
palindromenum=[5,6,7,9,11,12,14,15,17,18,19,21,28,35,36,37,42,63,73,74,84,85,94,101,111,119,126,131,185,202,303,404,409]
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

def mainpage(level,sad, sick, angry,happy):
    if level == 10:
        "GameOver"
    elif level == range(7,9):
        if sick > 0:
            "starsick"
        elif angry >0:
            "starangry"
        elif sad > 0:
            "starsad"
        else :
            if happy > 8:
                "superhappystar"
            elif happy == range(7,8):
                "happystar"
            elif happy == range(5,6):
                "averagestar"
            else:
                "sadstar"
    elif level ==range(3,6):
        if sick > 0:
            "nebulasick"
        elif angry >0:
            "nebulaangry"
        elif sad > 0:
            "nebulasad"
        else :
            if happy > 8:
                "superhappynebula"
            elif happy == range(7,8):
                "happynebula"
            elif happy == range(5,6):
                "averagenebula"
            else:
                "sadnebula"
    else :
        if sick > 0:
            "gassick"
        elif angry >0:
            "gasangry"
        elif sad > 0:
            "gassad"
        else :
            if happy > 8:
                "superhappygas"
            elif happy == range(7,8):
                "happygas"
            elif happy == range(5,6):
                "averagegas"
            else:
                "sadgas"
    
        
