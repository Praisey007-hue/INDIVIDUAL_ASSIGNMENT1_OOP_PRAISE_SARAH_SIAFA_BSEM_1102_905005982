"""Core portal operations, implemented with object-oriented programming."""
from student import Student
from course import Course


class LearningPortal:
    """Manage students and courses using a dictionary data structure."""

    portal_count = 0

    def __init__(self, name):
        self.name = name
        # The assignment permits one data structure; dictionaries are used
        # as the main record store, keyed by unique IDs.
        self.students = {}
        self.courses = {}
        LearningPortal.portal_count += 1

    @classmethod
    def get_portal_count(cls):
        """Class method: return the number of portal objects created."""
        return cls.portal_count

    @staticmethod
    def normalise_id(value):
        """Static helper: standardise an ID before looking it up."""
        return value.strip().upper()

    def add_student(self, student_id, name, programme):
        """Instance method: validate and add a student record."""
        key = self.normalise_id(student_id)
        if key in self.students:
            raise ValueError(f"Student ID {key} already exists.")
        self.students[key] = Student(key, name, programme)

    def add_course(self, course_id, title, instructor, lessons):
        """Add a course to the portal."""
        key = self.normalise_id(course_id)
        if key in self.courses:
            raise ValueError(f"Course ID {key} already exists.")
        self.courses[key] = Course(key, title, instructor, lessons)

    def enrol_student(self, student_id, course_id):
        """Enrol a student in an existing course."""
        student_key = self.normalise_id(student_id)
        course_key = self.normalise_id(course_id)
        if student_key not in self.students:
            raise ValueError("Student not found. Check the student ID.")
        if course_key not in self.courses:
            raise ValueError("Course not found. Check the course ID.")
        self.students[student_key].enrol(course_key)

    def mark_lesson_complete(self, student_id, course_id, lesson_title):
        """Record lesson completion after checking enrolment and lesson."""
        student_key = self.normalise_id(student_id)
        course_key = self.normalise_id(course_id)
        if student_key not in self.students:
            raise ValueError("Student not found.")
        if course_key not in self.courses:
            raise ValueError("Course not found.")
        student = self.students[student_key]
        course = self.courses[course_key]
        if course_key not in student.enrolled_courses:
            raise ValueError("Student must enrol in this course first.")
        matching_lesson = next(
            (lesson for lesson in course.lessons
             if lesson.casefold() == lesson_title.strip().casefold()),
            None
        )
        if matching_lesson is None:
            raise ValueError("That lesson is not listed in the selected course.")
        student.mark_lesson_complete(course_key, matching_lesson)

    def display_students(self):
        print("\n--- STUDENTS ---")
        if not self.students:
            print("No students have been registered.")
            return
        for student in self.students.values():
            print(student.display_info())

    def display_courses(self):
        print("\n--- COURSES ---")
        if not self.courses:
            print("No courses are available.")
            return
        for course in self.courses.values():
            print(course.display_info())
            for number, lesson in enumerate(course.lessons, start=1):
                print(f"   {number}. {lesson}")

    def display_dashboard(self, student_id):
        key = self.normalise_id(student_id)
        student = self.students.get(key)
        if student is None:
            print("Student not found. Check the student ID.")
            return
        print(f"\n--- LEARNING DASHBOARD: {student.name} ---")
        print(student.display_info())
        if not student.enrolled_courses:
            print("You are not enrolled in any courses yet.")
            return
        for course_id in student.enrolled_courses:
            course = self.courses[course_id]
            completed = student.completed_lessons.get(course_id, [])
            total = len(course.lessons)
            percent = int((len(completed) / total) * 100) if total else 0
            print(f"\n{course.title}: {len(completed)}/{total} lessons complete ({percent}%)")
            for lesson in course.lessons:
                status = "DONE" if lesson in completed else "TODO"
                print(f"   [{status}] {lesson}")

    def display_summary(self):
        print("\n--- PORTAL SUMMARY ---")
        print(f"Portal: {self.name}")
        print(f"Registered students: {len(self.students)}")
        print(f"Available courses: {len(self.courses)}")
        print(f"Portal objects created: {self.get_portal_count()}")

    def load_demo_data(self):
        """Create fictional sample data so the program is ready to demonstrate."""
        if not self.students:
            self.add_student("STU001", "Aminata Kamara", "Software Engineering")
            self.add_student("STU002", "David Conteh", "Information Technology")
        if not self.courses:
            self.add_course(
                "CS101", "Introduction to Programming", "Ms. Johnson",
                ["Getting Started with Python", "Variables and Data Types",
                 "Conditions and Loops"]
            )
            self.add_course(
                "DB102", "Database Fundamentals", "Mr. Sesay",
                ["What Is a Database?", "Tables and Records",
                 "Introduction to SQL"]
            )
        self.enrol_student("STU001", "CS101")
        self.enrol_student("STU001", "DB102")
        self.enrol_student("STU002", "CS101")
