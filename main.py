import json
import os

FILENAME = "students.json"


def load_data():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return json.load(file)


def save_data(data):
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)


def add_student(data):
    name = input("Enter student name: ")
    score = float(input("Enter score: "))

    data.append({"name": name, "score": score})
    save_data(data)

    print("✅ Student added!")


def view_students(data):
    if not data:
        print("No students found.")
        return

    for i, student in enumerate(data, 1):
        print(f"{i}. {student['name']} - {student['score']}")


def search_student(data):
    name = input("Enter name to search: ")

    for student in data:
        if student["name"].lower() == name.lower():
            print(f"Found: {student['name']} - {student['score']}")
            return

    print("❌ Student not found.")


def delete_student(data):
    name = input("Enter name to delete: ")

    for student in data:
        if student["name"].lower() == name.lower():
            data.remove(student)
            save_data(data)
            print("✅ Deleted successfully.")
            return

    print("❌ Student not found.")


def analyze(data):
    if not data:
        print("No data to analyze.")
        return

    avg = sum(s["score"] for s in data) / len(data)
    top = max(data, key=lambda x: x["score"])

    print(f"📊 Average Score: {avg:.2f}")
    print(f"🏆 Top Student: {top['name']} ({top['score']})")


def menu():
    data = load_data()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Analyze Data")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_student(data)
        elif choice == "2":
            view_students(data)
        elif choice == "3":
            search_student(data)
        elif choice == "4":
            delete_student(data)
        elif choice == "5":
            analyze(data)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


menu()