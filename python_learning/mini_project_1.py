from random import *
n = int(input("Введите границу диапазона числа"))
number = randint(1,n)
count = 0

print("Добро пожаловать в числовую угадайку")

def is_valid(text, n):
    
    if text.isdigit():
        num = int(text)
        
        if 1 <= num <= n:
            return True
        
    return False

while True:
    num = input("Введите число: ")
    
    if not is_valid(num, n):
        print(f"А может быть все-таки введем целое число от 1 до {n}?")
        continue
    
    num = int(num)
    count += 1
    
    if num > number:
        print("Ваше число больше загаданного, попробуйте еще разок")
        
    elif num < number:
        print("Ваше число меньше загаданного, попробуйте еще разок")
        
    elif num == number:
        print("Вы угадали, поздравляем!")
        print(f"Вами было потрачено {count} попыток")
        break
print("Спасибо, что играли в числовую угадайку. Еще увидимся...")