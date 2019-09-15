"""
Домашнее задание №1
Условный оператор: Сравнение строк
* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты
"""

def check_strings(incoming_string_one, incoming_string_two):
    from collections import Counter
    if type(incoming_string_one) != str or type(incoming_string_two) != str:
        return 0
    else:
        if Counter(incoming_string_one) == Counter(incoming_string_two):
            return 1
        else:
            if len(incoming_string_one) > len(incoming_string_two):
                return 2
            elif incoming_string_two == 'learn':
                return 3  
    
if __name__ == "__main__":
    print(check_strings("1",2))
    print(check_strings("heyworld","learn"))
    print(check_strings("learn","learn"))
    print(check_strings("heyworld","learn123"))
    print(check_strings("hey","learn"))





  
    
