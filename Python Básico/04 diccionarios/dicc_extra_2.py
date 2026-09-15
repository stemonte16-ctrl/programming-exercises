employees = [
    {
        "name": "Carlos",
        "email": "carlos@empresa.com",
        "department": "Ventas"
    },
    {
        "name": "Ana",
        "email": "ana@empresa.com",
        "department": "TI"
    },
    {
        "name": "Luis",
        "email": "luis@empresa.com",
        "department": "Ventas"
    },
    {
        "name": "Sofía",
        "email": "sofia@empresa.com",
        "department": "RRHH"
    }
]

result = {}

for employee in employees:
    department = employee["department"]

    if department not in result:
        result[department] = []

    result[department].append(employee)

print(result)