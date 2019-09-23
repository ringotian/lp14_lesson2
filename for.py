
"""
Домашнее задание №1
Цикл for: Оценки
* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

#Task slides #1
list = [item for item in range(10)]
for i in list:
    print(i+1)

#Task slides #2
incoming_str = input("Enter str: ")
for i in incoming_str:
    print(i)

#Task #3
marks = [{'school_class': '4a', 'scores': [2,4,4,5,2]},
        {'school_class': '4b', 'scores': [1,4,5,5,2,5]},
        {'school_class': '5a', 'scores': [5,5,3,4,2]},
        {'school_class': '4b', 'scores': [2,4,3,3,5,5,2]}]

average_school_marks = 0
counter = 0

for mark in marks:
    average_class_marks = sum(mark['scores'])/len(mark['scores'])
    print(f"Average score for class {mark['school_class']} is {average_class_marks}")
    # можно сделать проще
    counter = counter + len(mark['scores'])
    average_school_marks = average_school_marks + sum(mark['scores'])
    # for i in mark['scores']:
    #     counter = counter + 1
    #     average_school_marks = average_school_marks + i
average_school_marks = average_school_marks / counter
print(f"Average score for school is {average_school_marks}") 