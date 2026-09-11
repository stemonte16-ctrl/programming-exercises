import csv

student_list = []


def export_students(file_path):
    # Exports all students from the list to a CSV file.
    if len(student_list) == 0:
        print("No hay estudiantes registrados para exportar.")
        return

    fieldnames = [
        "name",
        "section",
        "spanish_grade",
        "english_grade",
        "social_grade",
        "science_grade",
        "math_grade"
    ]

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(student_list)

    print("Estudiantes exportados correctamente.")


def import_students(file_path):
    # Imports students from a CSV file into the student list.
    try:
        with open(file_path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            student_list.clear()

            for row in reader:
                student = {
                    "name": row["name"],
                    "section": row["section"],
                    "spanish_grade": float(row["spanish_grade"]),
                    "english_grade": float(row["english_grade"]),
                    "social_grade": float(row["social_grade"]),
                    "science_grade": float(row["science_grade"]),
                    "math_grade": float(row["math_grade"])
                }

                student_list.append(student)

        print("Estudiantes importados correctamente.")

    except FileNotFoundError:
        print("No existe un archivo de estudiantes para importar.")

    except (KeyError, ValueError):
        print("El archivo CSV no tiene un formato válido.")