Students Management System

A simple command-line student management system built with Python. This application allows you to register, view, search, update, and delete student records with persistent data storage using JSON.
✨ Features

    ✅ Register new students with ID, name, age, program, and status
    ✅ View all students in a formatted list
    ✅ Search students by ID
    ✅ Update student information
    ✅ Delete students by ID
    ✅ Persistent data storage (JSON file)
    ✅ Input validation using utility functions
    ✅ User-friendly menu interface

📋 Requirements

    Python 3.6+
    No external dependencies (uses only standard library)

🛠️ Project Structure

students-management/
│
├── main.py              # Main application file (your code)
├── utils/
│   └── valid.py         # Utility functions (pedir_entero, pedir_estado, pedir_plan)
└── students.json        # Generated data file (created automatically)

🚀 Quick Start

    Save the code as main.py

    Ensure utils/valid.py exists with the required functions:

    python
    # utils/valid.py
    def pedir_entero(mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Please enter a valid number.")

    def pedir_estado():
        while True:
            estado = input("Status (active/inactive): ").lower()
            if estado in ['active', 'inactive']:
                return estado
            print("Please enter 'active' or 'inactive'.")

    def pedir_plan():
        planes = ['Computer Science', 'Engineering', 'Business', 'Medicine']
        print("Available programs:", ", ".join(planes))
        return input("Enter program: ")

    Run the application:

    bash
    python main.py

📱 Usage

 STUDENTS MANAGMENT SYSTEM
1. Register Student
2. Show Students  
3. Find Student
4. Update Student
5. Delete Student
6. EXIT

Example Workflow:

    Choose 1 → Register a new student
    Choose 2 → View all students
    Choose 3 → Search by ID
    Choose 4 → Update student details
    Choose 5 → Delete student
    Choose 6 → Exit

💾 Data Persistence

    All student data is automatically saved to students.json
    Data is loaded automatically when the program starts
    No data loss between sessions

Sample students.json:

json
[
    {
        "id": 123,
        "name": "John Doe",
        "age": 20,
        "program": "Computer Science",
        "status": "active"
    }
]

🐛 Troubleshooting

Issue
	

Solution

NameError: name 'students' is not defined
	

Add students = load_students() at the end of your file

ModuleNotFoundError: No module named 'utils.valid'
	

Create utils/valid.py with the required functions

Duplicate ID error
	

ID already exists, choose a unique ID
🔮 Future Improvements

    [ ] Export to CSV/Excel
    [ ] Search by name/program
    [ ] Age validation
    [ ] Bulk operations
    [ ] Web interface (Flask/Django)
    [ ] Database integration (SQLite)

📄 License

This project is open source and available under the MIT License.
