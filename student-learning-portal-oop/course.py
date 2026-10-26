"""Course domain model for the LearnSpace portal."""


class Course:
    """Represent a course and its lessons."""

    def __init__(self, course_id, title, instructor, lessons):
        if not course_id.strip() or not title.strip():
            raise ValueError("Course ID and title are required.")
        self.course_id = course_id.strip().upper()
        self.title = title.strip()
        self.instructor = instructor.strip() or "Not assigned"
        self.lessons = [lesson.strip() for lesson in lessons if lesson.strip()]

    def display_info(self):
        """Return a readable course summary."""
        return (
            f"{self.course_id} — {self.title} | Instructor: {self.instructor} "
            f"| Lessons: {len(self.lessons)}"
        )
