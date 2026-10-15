numbers = []

for i in range(10):
    number = int(input("Ingrese un número: "))
    numbers.append(number)

highest = numbers[0]

for number in numbers:
    if number > highest:
        highest = number

print(numbers)
print("El más alto fue", highest)