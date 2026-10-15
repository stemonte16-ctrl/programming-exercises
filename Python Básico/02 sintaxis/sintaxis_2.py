name = input("Ingrese su nombre: ")
lastname = input("Ingrese su apellido: ")
age = int(input("Ingrese su nombre: "))

if age >= 65:
    print(f"Hola {name} {lastname} usted es adulto mayor")
elif age >= 25:
    print(f"Hola {name} {lastname} usted es un adulto")
elif age >= 18:
    print(f"Hola {name} {lastname} usted es adulto joven")
elif age >= 16:
    print(f"Hola {name} {lastname} usted es adolecente")
elif age >= 13:
    print(f"Hola {name} {lastname} usted es preadolecente")
elif age >= 5:
    print(f"Hola {name} {lastname} usted es niño")
else:
    print(f"Hola {name} {lastname} usted es un bebé")