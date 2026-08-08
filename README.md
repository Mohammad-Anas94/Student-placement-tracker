# Student-placement-tracker
Developed a Python-based Student Placement Tracker to manage internship and placement applications. Implemented CRUD operations, JSON-based data storage, search and status tracking, placement statistics, input validation, exception handling, and OOP principles for a structured and maintainable application.




# 🎓 Student Placement Tracker

A Python-based **Student Placement Tracker** designed to help students manage and monitor their internship and placement applications from a simple command-line interface.

The application stores data permanently using **JSON file handling** and provides features for adding, searching, updating, deleting, and analyzing placement applications.

---

## 📌 Features

* ➕ Add new internship/placement applications
* 📋 View all applications
* 🔍 Search applications by company or role
* 🔄 Update application status
* 🗑️ Delete applications
* 📊 View placement statistics
* 💾 Persistent data storage using JSON
* 🛡️ Input validation and exception handling
* 🧱 Object-Oriented Programming structure

### Application Statuses

The tracker supports the following application stages:

* Applied
* Shortlisted
* Interview
* Selected
* Rejected

---

## 🛠️ Technologies Used

* **Python 3**
* Object-Oriented Programming (OOP)
* JSON
* File Handling
* Exception Handling
* Git & GitHub

No external Python libraries are required.

---

## 📂 Project Structure

```text
Student-Placement-Tracker/
│
├── placement_tracker.py
├── applications.json
├── README.md
│
└── screenshots/
    ├── menu.png
    ├── applications.png
    └── statistics.png
```

> `applications.json` is automatically created when application data is saved.

---

## ⚙️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/student-placement-tracker.git
```

### 2. Navigate to the project directory

```bash
cd student-placement-tracker
```

### 3. Run the program

```bash
python placement_tracker.py
```

---

## 🖥️ Main Menu

```text
========================================
       STUDENT PLACEMENT TRACKER
========================================

1. Add Application
2. View Applications
3. Search Application
4. Update Status
5. Delete Application
6. Placement Statistics
7. Exit

Enter your choice:
```

---

## ➕ Adding an Application

The user can enter information such as:

```text
Company name: Google
Job role: ML Intern
Location: Hyderabad
Your CGPA: 8.2
```

The application is automatically saved with the status:

```text
Applied
```

---

## 🔄 Updating Application Status

Users can update an application's status using its ID.

Available statuses:

```text
1. Applied
2. Shortlisted
3. Interview
4. Selected
5. Rejected
```

For example:

```text
ID: 1
Company: Google
Role: ML Intern
Status: Interview
```

---

## 🔍 Searching Applications

Applications can be searched using the company name or job role.

Example:

```text
Enter company or role: google
```

The program displays matching applications.

---

## 📊 Placement Statistics

The application provides basic placement analytics.

Example:

```text
===== PLACEMENT STATISTICS =====

Total Applications : 10
Applied            : 4
Shortlisted        : 2
Interviews         : 2
Selected           : 1
Rejected           : 1
Selection Rate     : 10.0 %
```

The selection rate is calculated using:

```text
Selection Rate = (Selected Applications / Total Applications) × 100
```

---

## 💾 Data Storage

Application information is stored in a local JSON file.

Example:

```json
[
    {
        "id": 1,
        "company": "Google",
        "role": "ML Intern",
        "location": "Hyderabad",
        "cgpa": 8.2,
        "status": "Interview"
    }
]
```

This allows application data to remain available even after closing and restarting the program.

---

## 🧠 Python Concepts Demonstrated

This project was developed to apply fundamental Python programming concepts in a practical application.

### Core Python

* Variables
* Data types
* Conditional statements
* Loops
* Functions
* Lists
* Dictionaries

### Intermediate Python

* Classes and objects
* Constructors
* Methods
* File handling
* JSON data
* Exception handling
* Input validation
* Modules

---

## 🚀 Future Improvements

The project can be extended with:

* 🖥️ Tkinter graphical user interface
* 📅 Application and interview dates
* 🔔 Interview/deadline reminders
* 📈 Graphical placement analytics
* 👤 Student profile management
* 📄 Resume management
* 🔎 Advanced filtering
* 🗄️ SQLite/MySQL database
* 🌐 Web-based version using Flask or FastAPI
* 🔐 User authentication

---

## 🎯 Learning Objective

The main objective of this project is to strengthen practical Python programming skills by developing a complete application that uses:

```text
Python Basics
     ↓
Functions
     ↓
Data Structures
     ↓
File Handling
     ↓
JSON
     ↓
Exception Handling
     ↓
OOP
```

The project also provides a foundation for progressing toward larger applications involving databases, APIs, web development, and machine learning.

---

## 👨‍💻 Author

**Anas**

B.Tech — CSE (AI & ML)

---

## 📜 License

This project is created for **educational and portfolio purposes**.
