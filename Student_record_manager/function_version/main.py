
from student_manager import load_data, save_data, view_students, search_student, update_student, delete_student, add_student

data = load_data()


save_data(data)
while True:
    print("\nStudent Record Manager")
    print("1. View Students")
    print("2. Search Student")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Add New Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_students(data)

    elif choice == "2":
        search_student(data)

    elif choice == "3":
        update_student(data)

    elif choice == "4":
        delete_student(data)

    elif choice == "5":
        add_student(data)

    elif choice == "6":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")