import string
import random
LETTERS = string.ascii_letters
NUMBERS = string.digits  
PUNCTUATION = string.punctuation  

def passwordGenerator(n):
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz~!@-#$'
    password = ''
    for x in range(0,n):
        randomNumber = random.randint(0,n)
        password += chars[randomNumber]
    print(password)


passwordGenerator(10)