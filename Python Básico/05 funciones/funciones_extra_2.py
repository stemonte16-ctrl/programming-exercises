def filter_words(words, n):
    new_list = []

    for word in words:
        if len(word) > n:
            new_list.append(word)

    return new_list


words = ["cielo", "sol", "maravilloso", "día"]

n = int(input("Ingrese el numero de letras minimas en la palabra: "))

result = filter_words(words, n)

print(result)