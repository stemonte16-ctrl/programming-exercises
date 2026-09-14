import csv

student_list = []


def export_students(file_path, students):
    # Exports all students from the list to a CSV file.
    if len(students) == 0:
        print("No hay estudiantes registrados para exportar.")
        return

    fieldnames = [
        "name",
        "section",
        "spanish_grade",
        "english_grade",
        "social_grade",
        "science_grade"
    ]

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(students)

    print("Estudiantes exportados correctamente.")


def import_students(file_path, students):
    # Imports students from a CSV file into the student list.
    try:
        with open(file_path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            students.clear()

            for row in reader:
                student = {
                    "name": row["name"],
                    "section": row["section"],
                    "spanish_grade": float(row["spanish_grade"]),
                    "english_grade": float(row["english_grade"]),
                    "social_grade": float(row["social_grade"]),
                    "science_grade": float(row["science_grade"])
                }

                students.append(student)

        print("Estudiantes importados correctamente.")

    except FileNotFoundError:
        print("No existe un archivo de estudiantes para importar.")

    except (KeyError, ValueError):
        print("El archivo CSV no tiene un formato válido.")