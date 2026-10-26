"""LearnSpace Student Learning Portal — OOP1 assignment demo."""
from portal import LearningPortal


def main():
    portal = LearningPortal("LearnSpace Student Learning Portal")
    portal.load_demo_data()

    while True:
        print("\n" + "=" * 54)
        print(portal.name)
        print("=" * 54)
        print("1. Display all students")
        print("2. Add a student")
        print("3. Display all courses")
        print("4. Enrol a student in a course")
        print("5. View a student's learning dashboard")
        print("6. Mark a lesson complete")
        print("7. View portal summary")
        print("0. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            portal.display_students()
        elif choice == "2":
            student_id = input("Student ID (e.g. STU004): ").strip()
            name = input("Student name: ").strip()
            programme = input("Programme/course of study: ").strip()
            if not all((student_id, name, programme)):
                print("All fields are required.")
            else:
                try:
                    portal.add_student(student_id, name, programme)
                    print("Student added successfully.")
                except ValueError as exc:
                    print(f"Could not add student: {exc}")
        elif choice == "3":
            portal.display_courses()
        elif choice == "4":
            student_id = input("Student ID: ").strip()
            course_id = input("Course ID (e.g. CS101): ").strip()
            try:
                portal.enrol_student(student_id, course_id)
                print("Enrolment successful.")
            except ValueError as exc:
                print(f"Could not enrol student: {exc}")
        elif choice == "5":
            student_id = input("Student ID: ").strip()
            portal.display_dashboard(student_id)
        elif choice == "6":
            student_id = input("Student ID: ").strip()
            course_id = input("Course ID: ").strip()
            lesson = input("Lesson title: ").strip()
            try:
                portal.mark_lesson_complete(student_id, course_id, lesson)
                print("Lesson marked as complete.")
            except ValueError as exc:
                print(f"Could not update progress: {exc}")
        elif choice == "7":
            portal.display_summary()
        elif choice == "0":
            print("Thank you for using LearnSpace. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose one of the listed options.")


if __name__ == "__main__":
    main()
