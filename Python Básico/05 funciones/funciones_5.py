def sort_words(text):
    words = text.split("-")

    words.sort()

    result = "-".join(words)

    return result


my_string = "python-variable-funcion-computadora-monitor"

print(sort_words(my_string))