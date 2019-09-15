"""
Домашнее задание №1
Условный оператор: Возраст
* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран
"""

def main():
    age = float(input("Please, enter your age: "))
    if 0 <= age < 7:
        return "Are you in the kindergarten?"
    elif 7 <= age < 17:
        return "Are you in school?"
    elif 17 <= age <= 22:
        return "Are you studying at the university?"
    else:
        return "Are you working?"

if __name__ == "__main__":
    occupation_result = main()
    print(occupation_result)