my_list = [10, 20, 30, 40, 50]

total = 0

for number in my_list:
    total += number

average = total / len(my_list)

new_list = []

for number in my_list:
    if number > average:
        new_list.append(number)

print("Promedio:", average)
print("Nueva lista:", new_list)