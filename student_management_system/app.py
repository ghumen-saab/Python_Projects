from student import(
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student
)
def show_menu():
    print("\n================================")
    print("  Student Management System")
    print("================================")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

def main():
    
    while True:

        show_menu()

        choice = input("\nEnter your choice(1-6): ")

        # Add a new student
        if choice == "1":

            print("\n=======Add New Student=======")

            name = input("Enter student name: ")

            if not name.strip():
                print("Name cannot be empty. Please try again.")
                continue

            try:
                age = int(input("Enter student age: "))

                if age <= 0:
                    print("Age must be greater than 0. Please try again.")
                    continue

            except ValueError:
                print("Age must be a valid integer. Please try again.")
                continue

            course = input("Enter student course: ")

            if not course.strip():
                print("Course cannot be empty. Please try again.")
                continue

            try:
                marks = float(input("Enter student marks (0-100): "))

                if marks < 0 or marks > 100:
                    print("Marks must be between 0 and 100. Please try again.")
                    continue

            except ValueError:
                print("Marks must be a valid number. Please try again.")
                continue

            add_student(name, age, course, marks)

        # View all students
        elif choice == "2":
            print("\n=======View All Students=======")

            view_students()

        # Search for a student by name
        elif choice == "3":

            print("\n=======Search Student=======")

            name = input("Enter student name: ")

            if not name.strip():
                print("Name cannot be empty. Please try again.")
                continue

            search_student(name)

        # Update an existing student's information
        elif choice == "4":
            print("\n=======Update Student=======")
            try:
                student_id = int(input("Enter student ID: "))
            except ValueError:
                print("Student ID must be a valid integer. Please try again.")
                continue

            update_student(student_id)

        # Delete a student by ID
        elif choice == "5":    
            print("\n=======Delete Student=======")
            try:
                student_id = int(input("Enter student ID: "))
            except ValueError:
                print("Student ID must be a valid integer. Please try again.")
                continue

            delete_student(student_id)

        # Exit the program
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")   

if __name__ == "__main__":
    main()            