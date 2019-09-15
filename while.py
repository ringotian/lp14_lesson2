
"""
Домашнее задание №1
Цикл while: ask_user
* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""

def ask_user():
    while True:
        fine = input("How are you? ")
        if fine == 'Fine':
            break

"""
Цикл while: ask_user со словарём
* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:
    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

def ask_user_modified():
    question_answer = {"How are you?": "Ok!", "What are you doing?": "I am eating", 
                    "What are you eating?": "Apples", "Is it tasty?": "Yes"}
    while True:
        question = input("Enter your question: ")
        if question in question_answer:
            print(question_answer[question])
        if question == "Quit":
            break
if __name__ == "__main__":
    ask_user_modified()
