# 🏥 Hospital Patient Record Management System

A simple yet functional **Python + SQLite** project to manage hospital patient records.  
This system allows adding, viewing, updating, and deleting patient records via a command-line interface.

---

## 📌 Features
- ➕ **Add Patient** – Register new patients with their details
- 📋 **View Patients** – Display all patient records
- ✏ **Update Patient** – Modify diagnosis & discharge date
- ❌ **Delete Patient** – Remove patient records
- 💾 **SQLite Database** – Lightweight and portable

---

## 🗂 Project Structure
hospital_patient_record_system/
│
├── main.py # Main program (menu & logic)
├── database.py # Database connection & table creation
├── requirements.txt # Dependencies (SQLite is built-in)
└── README.md # Project documentation

## run the program
python main.py

#example usage
=== Hospital Patient Record Management System ===
1. Add Patient
2. View Patients
3. Update Patient
4. Delete Patient
5. Exit
Enter choice: 1
Enter patient name: akhil
Enter age: 25
Enter gender: Male
Enter diagnosis: Fever
Enter admission date (YYYY-MM-DD): 2025-08-15
✅ Patient added successfully.

🛠 Technologies Used

Python 3

SQLite (Built-in)


🚀 Future Improvements

Add a GUI with Tkinter or PyQt

Export records to Excel / CSV

Add search functionality

📄 License

This project is open-source and available under the MIT License.


Developed by Nakka Vinay Kumar Goud
