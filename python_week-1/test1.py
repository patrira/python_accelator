

import os

FILENAME = "students.txt"

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    scores = []

    for i in range(1, 4):
        score = int(input(f"Enter Score for Subject {i}: "))
        scores.append(score)


    record = f"{roll},{name},{','.join(map(str, scores))}\n"


    with open(FILENAME, "a") as file:
        file.write(record)

    print("✅ Student added successfully.\n")

def display_students():
    if not os.path.exists(FILENAME):
        print("❌ No data found.")
        return

    with open(FILENAME, "r") as file:
        for line in file:
            roll, name, *scores = line.strip().split(",")
            scores = list(map(int, scores))
            total = sum(scores)
            avg = total / len(scores)
            print(f"Roll: {roll}, Name: {name}, Scores: {scores}, Total: {total}, Avg: {avg:.2f}")

def search_student():
    roll_search = input("Enter Roll Number to Search: ")
    found = False

    with open(FILENAME, "r") as file:
        for line in file:
            if line.startswith(roll_search + ","):
                print("✅ Record Found:")
                print(line.strip())
                found = True
                break

    if not found:
        print("❌ Student not found.")

def update_student():
    roll_update = input("Enter Roll Number to Update: ")
    updated = False
    lines = []

    with open(FILENAME, "r") as file:
        lines = file.readlines()

    with open(FILENAME, "w") as file:
        for line in lines:
            if line.startswith(roll_update + ","):
                print("✏️ Editing Record:", line.strip())
                name = input("Enter New Name: ")
                scores = [int(input(f"New Score for Subject {i+1}: ")) for i in range(3)]
                updated_line = f"{roll_update},{name},{','.join(map(str, scores))}\n"
                file.write(updated_line)
                updated = True
            else:
                file.write(line)

    if updated:
        print("✅ Record updated.")
    else:
        print("❌ Record not found.")

def delete_student():
    roll_delete = input("Enter Roll Number to Delete: ")
    deleted = False
    lines = []

    with open(FILENAME, "r") as file:
        lines = file.readlines()

    with open(FILENAME, "w") as file:
        for line in lines:
            if line.startswith(roll_delete + ","):
                deleted = True
                continue
            file.write(line)

    if deleted:
        print("🗑️ Record deleted.")
    else:
        print("❌ Record not found.")

def menu():
    while True:
        print("\n📘 STUDENT REPORT MANAGEMENT SYSTEM 📘")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Select an option (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("👋 Exiting program.")
            break
        else:
            print("⚠️ Invalid choice. Try again.")


menu()
