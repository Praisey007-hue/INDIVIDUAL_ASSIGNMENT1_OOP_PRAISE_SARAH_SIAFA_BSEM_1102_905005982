# LearnSpace — Student Learning Portal (OOP1)

**Course:** PROG211 — Object-Oriented Programming 1  
**Assignment:** Real-World Solutions under Digital Public Good (DPG) Standards  
**Chosen domain:** Education — Student Learning Portal  
**Language:** Python 3  
**Dependencies:** Python standard library only

## 1. Project overview

LearnSpace is a small command-line Student Learning Portal prototype. It demonstrates how object-oriented programming can help organise learning records. It lets a user register students, list courses, enrol students, record lesson completion, and view a learning dashboard.

The application uses fictional sample records only. It is an educational prototype, not a production system and does not collect passwords, addresses, phone numbers, grades, or other sensitive personal information.

## 2. Features

- Create and display student records.
- Create and display course records and lesson lists.
- Enrol a student in a course.
- Record lesson completion.
- Display a student's course progress.
- Display a portal summary.
- Validate IDs and reject duplicate student/course IDs.
- Preload fictional demo students and courses.

## 3. Project structure

```text
student-learning-portal-oop/
├── main.py       # Menu and user interaction
├── student.py    # Student class
├── course.py     # Course class
├── portal.py     # LearningPortal class and business logic
├── README.md     # Project documentation
└── CONTRIBUTING.md
```

## 4. Requirements

Install Python 3.9 or newer. No external Python packages are required.

Check your Python installation:

```bash
python --version
```

On some Windows computers, use:

```bash
py --version
```

## 5. Run in VS Code

1. Extract the project ZIP.
2. Open the extracted folder in Visual Studio Code.
3. Open **Terminal → New Terminal**.
4. Run:

   ```bash
   python main.py
   ```

   If `python` is not recognised on Windows, try:

   ```bash
   py main.py
   ```

5. Use the numbered menu. The demo data is loaded automatically.

## 6. Example usage

At launch, choose option `1` to display the sample students. Choose option `3` to display courses. The demo records include:

- Student `STU001` — Aminata Kamara
- Course `CS101` — Introduction to Programming
- Lessons: Getting Started with Python, Variables and Data Types, Conditions and Loops

Example workflow:

1. Choose `5` and enter `STU001` to view the dashboard.
2. Choose `6`, enter `STU001`, `CS101`, and `Getting Started with Python`.
3. Choose `5` again to see the lesson marked `DONE` and progress updated.
4. Choose `2` to add another student.
5. Choose `4` to enrol a student in a course.

Sample output (format may vary slightly):

```text
--- LEARNING DASHBOARD: Aminata Kamara ---
ID: STU001 | Name: Aminata Kamara | Programme: Software Engineering | Enrolled courses: 2

Introduction to Programming: 0/3 lessons complete (0%)
   [TODO] Getting Started with Python
   [TODO] Variables and Data Types
   [TODO] Conditions and Loops
```

After marking the first lesson complete, the course progress becomes `1/3 lessons complete (33%)`.

## 7. How the project meets the assignment tasks

### Task 1 — OOP basics

The project includes three relevant classes:

- `Student` in `student.py`
- `Course` in `course.py`
- `LearningPortal` in `portal.py`

Each class has attributes and methods. Examples include student ID, name, programme, enrolled courses, and completed lessons; and course ID, title, instructor, and lessons. `display_info()` methods return information about objects. The program creates objects and the portal calls their methods.

### Task 2 — Python data structure

A **dictionary** is used as the main record store:

- `self.students` stores `Student` objects using student IDs as keys.
- `self.courses` stores `Course` objects using course IDs as keys.

This supports adding records, finding records by ID, checking duplicates, and iterating through records for display. Lists are used inside each object for course enrolments and lesson collections as part of the domain model.

### Task 3 — Methods and DPG alignment

- **Instance methods:** `add_student()`, `enrol_student()`, `mark_lesson_complete()`, `display_dashboard()`.
- **Class method:** `LearningPortal.get_portal_count()` uses `@classmethod` to report how many portal objects have been created.
- **Static method:** `LearningPortal.normalise_id()` uses `@staticmethod` to standardise identifiers.
- **Open-source:** the source code can be shared and modified; add it to a public GitHub repository for submission.
- **Inclusive and accessible:** a plain-text numbered menu, clear prompts, and readable status labels do not depend on colour, images, or a mouse.
- **Privacy-respecting:** fictional examples only; no sensitive personal data is required.
- **Modular and reusable:** student, course, portal logic, and user interface are separated into individual Python files.

## 8. Object-oriented programming concepts demonstrated

- **Class:** a blueprint, such as `Student`.
- **Object:** an instance such as the student stored under `STU001`.
- **Attributes:** data held by an object, such as `student.name`.
- **Methods:** functions defined in a class, such as `student.display_info()`.
- **Encapsulation:** student and course data and related behaviour are grouped inside their classes.
- **Composition:** `LearningPortal` manages `Student` and `Course` objects.

## 9. Testing checklist

Before submitting, run the program and verify:

- [ ] The menu starts without an error.
- [ ] Demo students and courses display.
- [ ] A new student can be added.
- [ ] A duplicate student ID is rejected.
- [ ] A student can be enrolled in an existing course.
- [ ] Invalid student/course IDs show a useful message.
- [ ] A lesson can be marked complete only for an enrolled course.
- [ ] The dashboard shows updated progress.
- [ ] The summary displays record counts.

For the hardcopy, take screenshots of the running menu, student list, course list, and a dashboard after completing a lesson.

## 10. Limitations and future improvements

This is a small command-line assignment prototype. Records are held in memory and reset when the program exits. Future versions could add file/database persistence, teacher accounts, quizzes, assignment uploads, authentication, and a graphical or web interface. Those features are outside the core scope of this OOP1 brief.

## 11. GitHub submission

Create a new repository on GitHub, then run these commands from the project folder:

```bash
git init
git add .
git commit -m "Build LearnSpace student learning portal"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with the URL of your own repository. Add your lecturer as a repository collaborator as instructed in the assignment brief.

## 12. Academic integrity

Be prepared to explain the classes, dictionary, object creation, instance method, class method, and DPG choices in your own words. Review and personalise the code and documentation before submission.
