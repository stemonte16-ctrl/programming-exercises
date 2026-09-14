# This module contains the functions that perform the main actions of the system.
# Each function receives the student list and performs a specific operation.

def add_students(students):
    # Adds one or more students, validates their information,
    # and allows the user to continue adding students.

    should_continue = True

    while should_continue:

        # Validate student name
        while True:
            name = input("Ingrese el nombre del estudiante que desea agregar: ").title()

            if not is_valid_name(name):
                print("Nombre inválido. Intente nuevamente.")
                continue

            break

        # Validate student section
        while True:
            section = input("Ingrese la sección del estudiante: ")

            if not is_valid_section(section):
                print("Sección inválida. Intente nuevamente.")
                continue

            break

        # Check for duplicate student
        if student_exist(students, name, section):
            print("Ya existe un estudiante con ese nombre y sección.")
            continue

        # Validate Spanish grade
        while True:
            try:
                spanish_grade = float(input("Ingrese la nota de español: "))

                if spanish_grade >= 0 and spanish_grade <= 100:
                    break
                else:
                    print("Nota inválida\nIntente otra vez!!")

            except ValueError:
                print("Valor equivocado")

        # Validate English grade
        while True:
            try:
                english_grade = float(input("Ingrese la nota de inglés: "))

                if english_grade >= 0 and english_grade <= 100:
                    break
                else:
                    print("Nota inválida\nIntente otra vez!!")

            except ValueError:
                print("Valor equivocado")

        # Validate Social Studies grade
        while True:
            try:
                social_grade = float(input("Ingrese la nota de Sociales: "))

                if social_grade >= 0 and social_grade <= 100:
                    break
                else:
                    print("Nota inválida\nIntente otra vez!!")

            except ValueError:
                print("Valor equivocado")

        # Validate Science grade
        while True:
            try:
                science_grade = float(input("Ingrese la nota de Ciencias: "))

                if science_grade >= 0 and science_grade <= 100:
                    break
                else:
                    print("Nota inválida\nIntente otra vez!!")

            except ValueError:
                print("Valor equivocado")



        student = {
            "name": name,
            "section": section,
            "spanish_grade": spanish_grade,
            "english_grade": english_grade,
            "social_grade": social_grade,
            "science_grade": science_grade
        }

        students.append(student)

        print("Estudiante agregado correctamente.")

        while should_continue:
            another_student = input(
                "Si desea agregar otro estudiante indique 'SI' "
                "para agregarlo o 'NO' para volver al menú principal: "
            ).lower()

            if another_student == "si":
                break

            elif another_student == "no":
                should_continue = False
                break

            else:
                print("Respuesta inválida.")
# Displays all registered students and their information.

def show_students(students):
    for student in students:
        print("=============================================")
        print(f"Nombre : {student['name']}")
        print(f"Sección : {student['section']}")
        print(f"Nota de español : {student['spanish_grade']}")
        print(f"Nota de inglés : {student['english_grade']}")
        print(f"Nota de sociales : {student['social_grade']}")
        print(f"Nota de ciencias : {student['science_grade']}")
        print()
        print("==============================================")

# Calculates the average grade of a single student.
def calculate_average(student):
    average = (student["spanish_grade"] + student["english_grade"] + student["social_grade"] + student["science_grade"]) / 4
        
    return average

# Sorts students by average grade and displays the three highest averages.
def show_top_3(students):
    sorted_students = sorted(students,key=calculate_average,reverse=True)
    for position, student in enumerate(sorted_students[0:3]):
        average = calculate_average(student)
        print(f"Top {position + 1}: {student["name"]}, Promedio:{average}")

# Calculates the average of all students' individual averages.
def calculate_general_average(students):
    if len(students) == 0:
        print("No hay estudiantes registrados")
        return
    total = 0
    for student in students:
        average = calculate_average(student)
        total = total + average
    general_average = total / len(students)
    return general_average

# Searches for a student by name and section and removes them after confirmation.
def delete_student(students):
    name = input("Ingrese el nombre del estudiante que desea eliminar: ").lower()
    section = input("Ingrese la seccion del estudiante que desea eliminar: ")
    
    found = False
    
    for student in students:
        if student["name"] == name and student["section"] == section:
            found = True
            
            while True:
                question = input("¿Esta seguro de eliminar el estudiante?: ").lower()
            
                if question == "si":
                    students.remove(student)
                    break
                
                elif question == "no":
                    print("Eliminación cancelada")
                    break
                
                else:
                    print("Respuesta inválida")
            break
        
    if not found:
        print("Estudiante inexistente")

def show_failed_students(students):
    
    for student in students:
        
        failed_subjects = []
        found = False
        
        subjects = {
            "Español": "spanish_grade",
            "Inglés": "english_grade",
            "Sociales": "social_grade",
            "Ciencias": "science_grade",
            "Matemáticas": "math_grade"
        }
        for subject, grade_key in subjects.items():
            if student[grade_key] < 60:
                found = True
                failed_subjects.append((subject, student[grade_key]))
        if found:
            print("=" * 45)
            print(f"Nombre: {student["name"]}")
            print(f"Sección: {student["section"]}")
            print("Materias reprobadas:")
            
            for subject, grade in failed_subjects:
                print(f"{subject}: {grade}")
            
            print("=" * 45)

# This function is to see if the name is valid

def is_valid_name(name):
    
    if name.strip() == "":
        return False
    
    elif not name.replace(" ", "").isalpha():
        return False
    return True

# This function is to validate the section number

def is_valid_section(section):
    
    if len(section) != 3:
        return False
    elif not section[0:2].isdigit():
        return False
    elif not section[2].isalpha():
        return False
    return True

def student_exist(students,name,section):
    
    for student in students:
        if student["name"] == name and student["section"] == section:
            return True
    
    return False

def show_student_average(students):
    name = input("Ingrese el nombre del estudiante que desea consultar el promedio: ").title()
    
    section = input("Ingrese la section del estudiante: ")
    
    found = False
    for student in students:
        if student["name"] == name and student["section"] == section:
            found = True
            average = calculate_average(student)
            print(f"Nombre: {student["name"]}")
            print(f"Sección: {student["section"]}")
            print(f"Promedio: {average}")
            break
    if not found:
        print("Estudiante inexistente")