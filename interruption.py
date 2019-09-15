"""
Домашнее задание №1
Исключения: KeyboardInterrupt
* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    question_answer = {"How are you?": "Ok!", "What are you doing?": "I am eating", 
                    "What are you eating?": "Apples", "Is it tasty?": "Yes"}
    while True:
        try:
            question = input("Enter your question: ")
            if question in question_answer:
                print(question_answer[question])
            if question == "Quit":
                break
        except KeyboardInterrupt:
            print("Bye bye")
            break


'''
Перепишите функцию discounted(price, discount, max_discount=20)из урока про функции так, 
чтобы она перехватывала исключения, когда переданы некорректные аргументы 
(например, строки вместо чисел)'''


def discounted(price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(float(max_discount))
        if max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except (ValueError, TypeError):
        print("Inappropriate value")

'''
* Напишите функцию get_summ(num_one, num_two), которая принимает 
  на вход два целых числа (int), складывает их и возвращает результат 
  сложения
* Оба аргумента нужно приводить к целому числу при помощи int() и 
  перехватывать исключение ValueError если приведение типов не сработало
'''

def get_sum(num_one, num_two):
    try:
        return int(num_one) + int(num_two)
    except ValueError:
        print('Inappropriate value')



if __name__ == "__main__":
    ask_user()
    discounted(10,10)
    get_sum(1, '2')