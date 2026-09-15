def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for letter in text:
        if letter in vowels:
            count += 1

    return count


text = "Hola mundo"

result = count_vowels(text)

print(result)