number_of_notes = int(input("Ingrese el número de notas: "))

approved = 0
failed = 0
added = 0
added_approved = 0
added_failed = 0
for i in range(number_of_notes):
    note = float(input(f"Ingrese la nota {i + 1}: "))
    
    added += note

    if note >= 70:
        approved += 1
        added_approved += note
    else:
        failed += 1
        added_failed += note

average = added / number_of_notes

if approved > 0:
    average_approved = added_approved / approved
else:
    average_approved = 0

if failed > 0:
    average_failed = added_failed / failed
else:
    average_failed = 0
    
print(f"Aprobadas: {approved}")
print(f"Desaprobadas: {failed}")
print(f"Promedio total: {average}")
print(f"Promedio de las aprobadas: {average_approved}")
print(f"Promedio de las desaprobadas: {average_failed}")