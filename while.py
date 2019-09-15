def how_are_you():
    while True:
        fine = input("How are you? ")
        if fine == 'Fine':
            break

#how_are_you()

def how_are_you_modified():
    question_answer = {"How are you?": "Ok!", "What are you doing?": "I am eating", 
                    "What are you eating?": "Apples", "Is it tasty?": "Yes"}
    while True:
        question = input("Enter your question: ")
        if question in question_answer:
            print(question_answer[question])
        if question == "Quit":
            break
how_are_you_modified()
