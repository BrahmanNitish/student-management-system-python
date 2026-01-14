class Student:
    def __init__(self, roll, name, course):
        self.roll = roll
        self.name = name
        self.course = course

    def __str__(self):
        return f"{self.roll},{self.name},{self.course}"


class StudentManagementSystem:
    def __init__(self, filename="students.txt"):
        self.filename = filename

    def add_student(self):
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        course = input("Enter Course: ")

        student = Student(roll, name, course)

        with open(self.filename, "a") as file:
            file.write(str(student) + "\n")

        print("✅ Student added successfully!")

    def view_students(self):
        try:
            with open(self.filename, "r") as file:
                students = file.readlines()
                if not students:
                    print("⚠ No students found.")
                for s in students:
                    roll, name, course = s.strip().split(",")
                    print(f"Roll: {roll}, Name: {name}, Course: {course}")
        except FileNotFoundError:
            print("⚠ No data file found.")

    def search_student(self):
        roll_no = input("Enter Roll No to search: ")
        found = False

        try:
            with open(self.filename, "r") as file:
                for s in file:
                    roll, name, course = s.strip().split(",")
                    if roll == roll_no:
                        print(f"🎯 Found → Roll: {roll}, Name: {name}, Course: {course}")
                        found = True
                        break
            if not found:
                print("❌ Student not found.")
        except FileNotFoundError:
            print("⚠ No data file found.")

    def delete_student(self):
        roll_no = input("Enter Roll No to delete: ")
        students = []
        deleted = False

        try:
            with open(self.filename, "r") as file:
                students = file.readlines()

            with open(self.filename, "w") as file:
                for s in students:
                    roll, name, course = s.strip().split(",")
                    if roll != roll_no:
                        file.write(s)
                    else:
                        deleted = True

            if deleted:
                print("🗑 Student deleted successfully!")
            else:
                print("❌ Student not found.")

        except FileNotFoundError:
            print("⚠ No data file found.")


def main():
    sms = StudentManagementSystem()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            sms.add_student()
        elif choice == "2":
            sms.view_students()
        elif choice == "3":
            sms.search_student()
        elif choice == "4":
            sms.delete_student()
        elif choice == "5":
            print("👋 Exiting program...")
            break
        else:
            print("❌ Invalid choice!")


if __name__ == "__main__":
    main()
