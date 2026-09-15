def count_letters(text):
    upper_cases = 0
    lower_cases = 0

    for letter in text:
        if letter.isupper():
            upper_cases += 1
        elif letter.islower():
            lower_cases += 1

    print("There's", upper_cases, "upper cases and", lower_cases, "lower cases")


count_letters("I love Nación Sushi")