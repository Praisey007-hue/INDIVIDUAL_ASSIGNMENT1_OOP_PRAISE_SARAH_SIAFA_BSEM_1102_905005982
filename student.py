"""Student domain model for the LearnSpace portal."""


class Student:
    """Represent a learner using a non-sensitive demo identifier."""

    def __init__(self, student_id, name, programme):
        if not student_id.strip():
            raise ValueError("Student ID cannot be empty.")
        if not name.strip():
            raise ValueError("Student name cannot be empty.")
        if not programme.strip():
            raise ValueError("Programme cannot be empty.")

        self.student_id = student_id.strip().upper()
        self.name = name.strip()
        self.programme = programme.strip()
        self.enrolled_courses = []
        self.completed_lessons = {}

    def enrol(self, course_id):
        """Add a course to this student's enrolment list once."""
        course_id = course_id.strip().upper()
        if course_id not in self.enrolled_courses:
            self.enrolled_courses.append(course_id)

    def mark_lesson_complete(self, course_id, lesson_title):
        """Record a completed lesson for a course."""
        course_id = course_id.strip().upper()
        lesson_title = lesson_title.strip()
        if not lesson_title:
            raise ValueError("Lesson title cannot be empty.")
        self.completed_lessons.setdefault(course_id, [])
        if lesson_title not in self.completed_lessons[course_id]:
            self.completed_lessons[course_id].append(lesson_title)

    def display_info(self):
        """Return a readable student summary."""
        return (
            f"ID: {self.student_id} | Name: {self.name} | "
            f"Programme: {self.programme} | "
            f"Enrolled courses: {len(self.enrolled_courses)}"
        )
