import os

FILE_NAME = "employees.txt"

def add_employee():
    with open(FILE_NAME, "a") as file:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        
        record = f"{emp_id}, {name}, {position}, {salary}\n"
        file.write(record)
        print("Employee record added successfully!\n")

def view_employees():
    if not os.path.exists(FILE_NAME):
        print("No employee records found.\n")
        return
    with open(FILE_NAME, "r") as file:
        records = file.readlines()
        if not records:
            print("No employee records found.\n")
        else:
            for record in records:
                print(record.strip())

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    found = False
    if not os.path.exists(FILE_NAME):
        print("No employee records found.\n")
        return
    with open(FILE_NAME, "r") as file:
        for record in file:
            if record.startswith(emp_id + ","):
                print("Employee Found:", record.strip())
                found = True
                break
    if not found:
        print("Employee not found.\n")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    if not os.path.exists(FILE_NAME):
        print("No employee records found.\n")
        return
    with open(FILE_NAME, "r") as file:
        records = file.readlines()
    
    updated_records = []
    found = False

    for record in records:
        if record.startswith(emp_id + ","):
            found = True
            name = input("Enter new Name: ")
            position = input("Enter new Position: ")
            salary = input("Enter new Salary: ")
            updated_records.append(f"{emp_id}, {name}, {position}, {salary}\n")
        else:
            updated_records.append(record)
    
    if found:
        with open(FILE_NAME, "w") as file:
            file.writelines(updated_records)
        print("Employee record updated successfully!\n")
    else:
        print("Employee not found.\n")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    if not os.path.exists(FILE_NAME):
        print("No employee records found.\n")
        return
    with open(FILE_NAME, "r") as file:
        records = file.readlines()
    
    updated_records = [record for record in records if not record.startswith(emp_id + ",")]
    
    if len(updated_records) == len(records):
        print("Employee not found.\n")
    else:
        with open(FILE_NAME, "w") as file:
            file.writelines(updated_records)
        print("Employee record deleted successfully!\n")

def main():
    while True:
        print("\nEmployee Record Management")
        print("1. Add Employee Record")
        print("2. View All Employee Records")
        print("3. Search Employee by ID")
        print("4. Update Employee Information")
        print("5. Delete Employee Record")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
