import csv
import os

FILE = "students.csv"

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    file_exists = os.path.exists(FILE)

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["Name", "Roll Number", "Marks"])

        writer.writerow([name, roll, marks])

    print("Student added successfully!")

def view_students():
    try:
        with open(FILE, "r") as f:
            reader = csv.reader(f)

            for row in reader:
                print(row)

    except FileNotFoundError:
        print("No student records found.")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            add_student()
        elif choice == 2:
            view_students()
        elif choice == 3:
            print("Thank you!")
            break
        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid number!")
