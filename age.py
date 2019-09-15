age = float(input("Please, enter your age: "))

def occupation(age):
    if 3 <= age < 7:
        return "Are you in the kindergarten?"
    elif 7 <= age < 17:
        return "Are you in school?"
    elif 17 <= age <= 22:
        return "Are you studying at the university?"
    else:
        return "Are you working?"

occupation_result = occupation(age)
print(occupation_result)
   