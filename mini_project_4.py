eng_lower = "abcdefghijklmnopqrstuvwxyz"
eng_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rus_lower = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

direction = input("Сделайте выбор: (1 - шифровать или 2 - дешифровать)")
language = input("Выберите язык (1 - анг. , 2 - рус.): ")
step = int(input("Введите число сдвига: "))
text = input("Введите текст: ")

if direction == "2":
    step = -step
    
result = ""

for char in text:
    if char in eng_lower:
        index = eng_lower.find(char)
        new_index = (index + step) % 26
        result += eng_lower[new_index]

    elif char in eng_upper:
        index = eng_upper.find(char)
        new_index = (index + step) % 26
        result += eng_upper[new_index]
        
    elif char in rus_lower:
        index = rus_lower.find(char)
        new_index = (index + step) % 32
        result += rus_lower[new_index]
        
    elif char in rus_upper:
        index = rus_upper.find(char)
        new_index = (index + step) % 32
        result += rus_upper[new_index]

    else:
        result += char

print(f"Результат {result} ")


text = input().split()
eng_lower = "abcdefghijklmnopqrstuvwxyz"
eng_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = []

for word in text:
    word_len = 0
    for char in word:
        if char.isalpha():
            word_len += 1
            
    text2 = ""
    for char in word:
        if char in eng_lower:
            index = eng_lower.find(char)
            new_index = (index + word_len) % 26
            text2 += eng_lower[new_index]

        elif char in eng_upper:
            index = eng_upper.find(char)
            new_index = (index + word_len) % 26
            text2 += eng_upper[new_index]
        else:
            text2 += char
    result.append(text2)
print(" ".join(result))