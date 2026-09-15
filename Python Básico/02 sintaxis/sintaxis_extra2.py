user_time = float(input("Ingrese tiempo en segundos: "))

if user_time > 600:
    print("Mayor")
elif user_time < 600:
    remaining = 600 - user_time
    print(f"Para alcanzar los 10 minutos faltarian {remaining} segundos")
else:
    print("Igual")