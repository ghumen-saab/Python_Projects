import json
from pathlib import Path


Students_File = Path("students.json")

def load_students():
    """Load students from a JSON file."""

    if Students_File.exists():
        with Students_File.open("r") as file:
            return json.load(file)
    else:
        return []


def save_students(students):
    """Save students to a JSON file."""

    with Students_File.open("w") as file:
        json.dump(students, file, indent=4)


def calculate_grade(marks):
    """Calculate the grade based on marks."""

    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

def add_student(name, age, course, marks):
    """Add a new student to the list."""

    students = load_students()
    new_id = max(student["id"] for student in students) + 1 if students else 1
    new_student = {
        "id": new_id,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks,
        "grade": calculate_grade(marks)
    }
    students.append(new_student)
    save_students(students)
    print("Student added successfully.")
    print(f"Student ID: {new_id}, Name: {name}")


def view_students():
    """View all students."""

    students = load_students()
    if not students:
        print("No students found.")
        return
    print("\n=======List of Students=======")
    for student in students:
        grade = calculate_grade(student["marks"])
        print(f"""
ID     : {student["id"]}
Name   : {student["name"]}
Age    : {student["age"]}
Course : {student["course"]}
Marks  : {student["marks"]}
Grade  : {grade}
----------------------------------------
""")

def search_student(name):
    """Search for a student by ID and name."""

    students = load_students()
    found = False
    for student in students:
        if name.lower() in student["name"].lower():
            grade = calculate_grade(student["marks"])
            print(f"""
ID     : {student["id"]}
Name   : {student["name"]}
Age    : {student["age"]}
Course : {student["course"]}
Marks  : {student["marks"]}
Grade  : {grade}
----------------------------------------
""")
            found = True
    if not found:
        print("Student not found.")


def update_student(student_id):
    """Update an existing student's information."""

    students = load_students()

    for student in students:

        if student["id"] == student_id:

            print(f"Updating student: {student['name']}")

            name = input(
                f"Enter new name (press Enter to keep '{student['name']}'): "
            )

            age = input(
                f"Enter new age (press Enter to keep '{student['age']}'): "
            )

            course = input(
                f"Enter new course (press Enter to keep '{student['course']}'): "
            )

            marks = input(
                f"Enter new marks (press Enter to keep '{student['marks']}'): "
            )

            if name.strip():
                student["name"] = name

            if age.strip():
                student["age"] = int(age)

            if course.strip():
                student["course"] = course

            if marks.strip():
                student["marks"] = float(marks)

            student["grade"] = calculate_grade(student["marks"])


            save_students(students)

            print("Student updated successfully.")

            return
        
    print("Student not found.")              

def delete_student(student_id):
    """Delete a student by ID."""

    students = load_students()
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully.")
            return
    print("Student not found.")    