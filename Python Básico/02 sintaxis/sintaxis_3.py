import random

secret_number = random.randint(1,10)

while True:
    
    user_number = int(input("Adivine el numero del 1 al 10: "))
    
    if user_number == secret_number:
        print("Adivinaste, FELICIDADES!!!")
        break
    print("Icorrecto, intente otra vez")