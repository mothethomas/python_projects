import json

# ---------------- LOAD DATA ----------------
def load_data():
    try:
        with open("students.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return [
            {"name": "Anu", "marks": [80, 87, 98]},
            {"name": "Ann", "marks": [85, 86, 97]},
            {"name": "Meera", "marks": [92, 89, 95]}
        ]

# ---------------- SAVE DATA ----------------
def save_data(student_list):
    with open("students.json", "w") as file:
        json.dump(student_list, file, indent=4)

# ---------------- HELPER FUNCTION ----------------
def get_marks():
    try:
        m1 = int(input("Enter mark1: "))
        m2 = int(input("Enter mark2: "))
        m3 = int(input("Enter mark3: "))
        return [m1, m2, m3]
    except ValueError:
        print("Please enter only numbers for marks.")
        return None

# ---------------- VIEW STUDENTS ----------------
def view_students(student_list):
    topper_name = ""
    highest_average = 0

    print("\nDisplaying Student Details")
    print("_________________________")

    for student in student_list:
        total_marks = sum(student["marks"])   # improved
        average_marks = round(total_marks / len(student["marks"]), 2)

        if average_marks > highest_average:
            highest_average = average_marks
            topper_name = student["name"]

        print(f"Name: {student['name']}")
        print(f"Marks: {student['marks']}")
        print(f"Total marks: {total_marks}")
        print(f"Average: {average_marks}")
        print("____________________________")

    print(f"Highest Average: {highest_average}")
    print(f"Topper: {topper_name}")

# ---------------- SEARCH STUDENT ----------------
def search_student(student_list):
    search_name = input("Enter the student name to search: ")

    for student in student_list:
        if student["name"].lower() == search_name.lower():
            print(f"Name: {student['name']}")
            print(f"Marks: {student['marks']}")
            return

    print("Student not found.")

# ---------------- UPDATE STUDENT ----------------
def update_student(student_list):
    search_name = input("Enter the name to be updated: ")

    for student in student_list:
        if student["name"].lower() == search_name.lower():
            marks = get_marks()
            if marks:
                student["marks"] = marks
                save_data(student_list)
                print("Student updated successfully.")
                print(f"Name: {student['name']}")
                print(f"Marks: {student['marks']}")
            return

    print("Student not found.")

# ---------------- DELETE STUDENT ----------------
def delete_student(student_list):
    delete_name = input("Enter the name of the student to delete: ")

    for student in student_list:
        if student["name"].lower() == delete_name.lower():
            student_list.remove(student)
            save_data(student_list)
            print("Student removed successfully.")
            return

    print("Student not found.")

# ---------------- ADD STUDENT ----------------
def add_student(student_list):
    add_newstudent = input("Enter the name of new student: ")

    for student in student_list:
        if student["name"].lower() == add_newstudent.lower():
            print("Student already exists.")
            return

    marks = get_marks()
    if marks:
        newstudent = {"name": add_newstudent, "marks": marks}
        student_list.append(newstudent)
        save_data(student_list)
        print("Student added successfully.")
