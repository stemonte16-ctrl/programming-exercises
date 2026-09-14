from sistema_control_estudiantes.actions import add_students,show_students,show_student_average,show_top_3,calculate_general_average,delete_student,show_failed_students
from sistema_control_estudiantes.data import student_list,export_students,import_students
def show_menu():
    while True:
        
        print("===== SISTEMA DE ESTUDIANTES =====")
        print()
        print("1. Agregar estudiantes")
        print("2. Mostrar estudiantes")
        print("3. Top 3 de los mejores estudiantes")
        print("4. Promedio por estudiante")
        print("5. Promedio general de los estudiantes")
        print("6. Lista de estudiantes con 1 o más materias reprobadas")
        print("7. Eliminar estudiante")
        print("8. Exportar estudiantes a CSV")
        print("9. Importar estudiantes desde CSV")
        print("10. Salir")
        print()
        print("==================================")
        
        while True:
            try:
                option = int(input("Ingrese la opción que deseada:"))
                break
            except ValueError:
                print("Valor equivocado")
                
        if option == 1:
            add_students(student_list)
            
        elif option == 2:
            show_students(student_list)
            
        elif option == 3:
            show_top_3(student_list)
            
        elif option == 4:
            show_student_average(student_list)
            
        elif option == 5:
            general_average = calculate_general_average(student_list)
            
            if general_average is not None:
                print(f"Promedio general: {general_average}")
                
        elif option == 6:
            show_failed_students(student_list)
            
        elif option == 7:
            delete_student(student_list)
            
        elif option == 8:
            export_students("students.csv", student_list)
            
        elif option == 9:
            import_students("students.csv", student_list)
        
        elif option == 10:
            print("¡Gracias por usar nuestro sitema de estudiantes!")
            break
        else:
            print("Solo numeros dentro del rango del menú")