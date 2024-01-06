from db import DB


def main():
    db = DB("db.db")
    db.create_tables()
    
    while True:
        print("\n1. Додати нового студента")
        print("2. Додати новий курс")
        print("3. Показати список студентів")
        print("4. Показати список курсів")
        print("5. Зареєструвати студента на курс")
        print("6. Показати студентів на конкретному курсі")
        print("7. Вийти")

        choice = input("Оберіть опцію (1-7): ")

        if choice == "1":
            # Додавання нового студента     
            name = input("Введіть ім'я студента: ")
            while True:
                age = input("Введіть вік студента: ")
                try:
                    age = int(age)
                except:
                    print("Вік має бути числом")
                else:
                    break
            major = input("Введіть додаткову інформацію про студента: ")
            
            print(db.add_student(name, age, major))

        elif choice == "2":
            # Додавання нового курсу   
            name = input("Введіть назву курсе: ")
            instructor = input("Введіть ім'я викладача: ")
            
            print(db.add_course(name, instructor))

        elif choice == "3":
            # Показати список студентів
            print(db.get_all_students())
        
        elif choice == "4":
            # Показати список курсів
            print(db.get_all_courses())

        elif choice == "5":
            # Зареєструвати студента на курс
            student = input("Введіть ім'я/індекс студента: ")
            try:
                student = int(student)
            except:
                student = db.get_student_id_by_name(student)
            
            course = input("Введіть назву/індекс курсу: ")
            try:
                course = int(course)
            except:
                course = db.get_course_id_by_name(course)
            
            try:
                db.connect_student_to_course(student, course)
            except Exception as error:
                print("Помилка: \n", error)
            else:
                print("Студента успішно зареєстровано!")
            

        elif choice == "6":
            # Показати студентів на конкретному курсі
            course = input("Введіть назву/індекс курсу: ")
            try:
                course = int(course)
            except:
                course = db.get_course_id_by_name(course)
                
            print(db.get_students_on_course(course))
        
        elif choice == "7":
            break

        else:
            print("Некоректний вибір. Будь ласка, введіть число від 1 до 7.")
    



if __name__ == "__main__":
    main()
