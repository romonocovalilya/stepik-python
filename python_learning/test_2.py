# Проработать логику (напоминалка)

print("Итоговый экзамен по второму модулю")
print()
print("Решение задания №1")
print()
age = int(input())
digit2 = (age%100)//10
digit1 = age%10
if digit2 == 0 and digit1 == 0:
    print("YES")
else:
    print("NO")
print()
print("Решение задания №2")
print()
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (x1+y1+x2+y2)%2==0:
    print("YES")
else:
    print("NO")
print()
print("Решение задания №3")
print()
age = int(input())
floor = input()
if 10<=age<=15 and floor == "f":
    print("YES")
else:
    print("NO")
print()
print("Решение задания №4")
print()
num = int(input())

if num == 1:
    print("I")
elif num == 2:
    print("II")
elif num == 3:
    print("III")
elif num == 4:
    print("IV")
elif num == 5:
    print("V")
elif num == 6:
    print("VI")
elif num == 7:
    print("VII")
elif num == 8:
    print("VIII")
elif num == 9:
    print("IX")
elif num == 10:
    print("X")
else:
    print("ошибка")
print()
print("Решение задания №5")
print()
n = int(input())

if n%2 != 0:
    print("YES")
elif n%2==0 and 2<=n<=5:
    print("NO")
elif n%2==0 and 6<=n<=20:
    print("YES")
elif n%2==0 and n>20:
    print("NO")
print()
print("Решение задания №6")
print()
a, b, c, d = int(input()), int(input()), int(input()), int(input())

if (a - c)**2 == (b - d)**2:
    print("YES")
else:
    print("NO")
print()
print("Решение задания №7")
print()
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if abs((x1-x2)*(y1-y2)) == 2:
    print("YES")
else:
    print("NO")
print()
print("Решение задания №8")
print()
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (x1-x2)**2==(y1-y2)**2 or x1==x2 or y1==y2:
    print("YES")
else:
    print("NO")