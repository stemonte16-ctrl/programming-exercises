words = []

for i in range(5):
    word = input("Ingrese una palabra: ")
    words.append(word)

new_list = []

for word in words:
    if len(word) > 4:
        new_list.append(word)

print(new_list)