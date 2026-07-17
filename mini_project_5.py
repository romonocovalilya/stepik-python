def convert_base(num_str, base_from, base_to):
    dec_num = int(num_str, base_from)
    
    if base_to == 10:
        return str(dec_num)
    
    if base_to == 2:
        return bin(dec_num)[2:]
    
    elif base_to == 8:
        return oct(dec_num)[2:]
    
    elif base_to == 16:
        return hex(dec_num)[2:].upper()
    
    return "Ошибка: поддерживаются только системы 2, 8, 10, 16"

source_base = int(input("Из какой системы счисления переводим? (2, 8, 10, 16): "))
target_base = int(input("В какую систему счисления переводим? (2, 8, 10, 16): "))
number = input("Введите число для перевода: ")

result = convert_base(number, source_base, target_base)
print(f"Результат: {result}")