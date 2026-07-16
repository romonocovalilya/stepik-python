from random import *

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"

chars = ''
count = int(input("Введите количество паролей: "))
length = int(input("Введите длинну пароля: "))
dig = input("Включать ли цифры (0123456789)? (да/нет) ")
low_let = input("Включать ли строчные буквы (abcdefghijklmnopqrstuvwxyz)? (да/нет) ")
uppe_let = input("Включать ли прописные буквы (ABCDEFGHIJKLMNOPQRSTUVWXYZ?) (да/нет) ")
punc = input("Включать ли символы (!#$%&*+-=?@^_)? (да/нет) ")
isc = input("Исключать ли неоднозначные символы (il1Lo0O)? (да/нет) ")

if dig.lower() == "да":
    chars += digits
    
if uppe_let.lower() == "да":
    chars += uppercase_letters
    
if punc.lower() == "да":
    chars += punctuation
    
if low_let.lower() == "да":
    chars += lowercase_letters

if isc.lower() == "да":
         for c in "il1Lo0O":
             chars = chars.replace(c, "")
if not chars:
    chars = lowercase_letters

def generate_password(length, chars):
    password = ""
    for _ in range(length):
        password += choice(chars)
    return password
for i in range(count):
    print(generate_password(length, chars))