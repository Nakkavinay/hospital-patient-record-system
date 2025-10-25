from database import create_table, create_connection

def add_patient():
    conn = create_connection()
    cursor = conn.cursor()
    name = input("Enter patient name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")
    diagnosis = input("Enter diagnosis: ")
    admission_date = input("Enter admission date (YYYY-MM-DD): ")
    cursor.execute("INSERT INTO patients (name, age, gender, diagnosis, admission_date) VALUES (?, ?, ?, ?, ?)",
                   (name, age, gender, diagnosis, admission_date))
    conn.commit()
    conn.close()
    print("✅ Patient added successfully.")

def view_patients():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("⚠ No patients found.")
    conn.close()

def update_patient():
    conn = create_connection()
    cursor = conn.cursor()
    patient_id = input("Enter patient ID to update: ")
    new_diagnosis = input("Enter new diagnosis: ")
    discharge_date = input("Enter discharge date (YYYY-MM-DD): ")
    cursor.execute("UPDATE patients SET diagnosis = ?, discharge_date = ? WHERE id = ?",
                   (new_diagnosis, discharge_date, patient_id))
    conn.commit()
    print("✅ Patient record updated.")
    conn.close()

def delete_patient():
    conn = create_connection()
    cursor = conn.cursor()
    patient_id = input("Enter patient ID to delete: ")
    cursor.execute("DELETE FROM patients WHERE id = ?", (patient_id,))
    conn.commit()
    print("✅ Patient deleted successfully.")
    conn.close()

def main():
    create_table()
    while True:
        print("\n=== Hospital Patient Record Management System ===")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Update Patient")
        print("4. Delete Patient")
        print("5. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            update_patient()
        elif choice == "4":
            delete_patient()
        elif choice == "5":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":4
main()