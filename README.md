# Student Management System

A simple **command-line Student Management System** built with Python. This project is designed to practice Python fundamentals, file handling, JSON data storage, functions, modules, CRUD operations, and input validation.

## Features

* Add a new student
* View all students
* Search students by name
* Update student information
* Delete students
* Automatically calculate student grades
* Store student data permanently in a JSON file
* Validate user input
* Modular project structure

## Project Structure

```text
student-management-system/
│
├── app.py              # Main application and menu
├── student.py          # Student management functions
├── students.json       # Student data storage
├── README.md           # Project documentation
└── .gitignore          # Files ignored by Git
```

## Student Information

Each student record contains:

* **ID** — Unique student identifier
* **Name** — Student's full name
* **Age** — Student's age
* **Course** — Student's course or degree
* **Marks** — Student's marks from 0 to 100
* **Grade** — Automatically calculated from marks

## Grade System

|  Marks | Grade |
| -----: | :---: |
| 80–100 |   A   |
|  70–79 |   B   |
|  60–69 |   C   |
|  50–59 |   D   |
|   0–49 |   F   |

## CRUD Operations

The application demonstrates the four basic CRUD operations:

```text
Create → Add Student
Read   → View/Search Students
Update → Update Student
Delete → Delete Student
```

## Technologies Used

* **Python 3**
* **JSON**
* File Handling
* Functions
* Modules
* Lists
* Dictionaries
* Loops
* Conditional Statements
* Exception Handling
* Input Validation

## Requirements

Make sure Python 3 is installed on your computer.

Check your Python version:

```bash
python --version
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/student-management-system.git
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Open the project

```bash
cd student-management-system
```

### 3. Create a virtual environment

Windows:

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

If you are using Command Prompt:

```cmd
venv\Scripts\activate
```

### 5. Run the application

```bash
python app.py
```

## Application Menu

When the application starts, you will see:

```text
================================
   STUDENT MANAGEMENT SYSTEM
================================
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit

Enter your choice (1-6):
```

## Example

### Add Student

```text
Enter your choice (1-6): 1

========== ADD STUDENT ==========

Enter student name: Ali Hassan
Enter student age: 22
Enter course: Software Engineering
Enter marks (0-100): 85

Student added successfully!
Student ID: 1
```

### View Students

```text
========== STUDENT LIST ==========

ID      : 1
Name    : Ali Hassan
Age     : 22
Course  : Software Engineering
Marks   : 85
Grade   : A
-----------------------------------
```

## Data Storage

Student records are stored in `students.json`.

Example:

```json
[
    {
        "id": 1,
        "name": "Ali Hassan",
        "age": 22,
        "course": "Software Engineering",
        "marks": 85,
        "grade": "A"
    }
]
```

The application reads the JSON file when it starts and saves changes whenever students are added, updated, or deleted.

## Learning Objectives

This project was created to practice:

1. Python functions
2. Python modules
3. Lists and dictionaries
4. Loops and conditions
5. User input
6. Input validation
7. Exception handling
8. File handling
9. JSON data storage
10. CRUD operations
11. Basic application architecture
12. Git and GitHub workflow

## Future Improvements

Possible improvements for future versions:

* Add student email and phone number
* Add student attendance
* Add multiple subjects and individual marks
* Calculate average marks
* Add GPA calculation
* Sort students by marks
* Search by student ID
* Add login/authentication
* Replace JSON with SQLite/MySQL
* Build a graphical user interface
* Create a REST API using FastAPI or Flask

## Author

**Ali Hassan**

Software Engineer | Python Learner | Aspiring AI Engineer

## License

This project is created for **learning and educational purposes**.



# Python CLI To-Do App

A command-line To-Do application built with Python.

## Features

- Add tasks
- View tasks
- Complete tasks
- Delete tasks
- Save tasks
- Load tasks

## Technologies

- Python
- JSON
- Git

## How to Run

Clone the repository:

git clone https://github.com/ghumen-saab/Python_Projects.git

Create virtual environment:

python -m venv venv

Activate environment.

Run:

python app.py
