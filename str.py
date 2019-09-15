from collections import Counter

def check_strings(incoming_string_one, incoming_string_two):
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
    
print(check_strings("1",2))
print(check_strings("heyworld","learn"))
print(check_strings("learn","learn"))
print(check_strings("heyworld","learn123"))
print(check_strings("hey","learn"))