import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

def password():
    parola = ""
    for i in range(8):
        parola += random.choice(karakterler)
    return parola

print(password())
    