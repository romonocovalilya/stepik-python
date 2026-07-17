def linear_search(my_list, target):

    for i in range(len(my_list)):

        if my_list[i] == target:
            return i  

    return -1 

numbers = [4, 2, 9, 7, 5, 1, 8]
target_element = 5

result_index = linear_search(numbers, target_element)

if result_index != -1:
    print(f"Элемент {target_element} найден под индексом: {result_index}") 
else:
    print(f"Элемента {target_element} нет в списке.")
