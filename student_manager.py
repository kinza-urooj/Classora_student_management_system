import json
import os
from student import Student

DATA_FILE = "students.json"

class StudentManager:
    """Handles student collection and JSON file storage."""

    def __init__(self):
        self.students = []
        self.load()

    def load(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r", encoding="utf-8") as file:
                    records = json.load(file)
                for record in records:
                    self.students.append(Student.from_dict(record))
            except (json.JSONDecodeError, KeyError, TypeError):
                self.students = []

    def save(self):
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump([student.to_dict() for student in self.students], file, indent=4)

    def add(self, student):
        self.students.append(student)
        self.save()

    def delete(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                self.save()
                return True
        return False

    def get_all(self):
        return self.students

    def get_stats(self):
        total = len(self.students)
        passed = 0
        failed = 0
        total_average = 0
        attendance_total = 0
        for student in self.students:
            if student.status == "Pass":
                passed += 1
            else:
                failed += 1
            total_average += student.average
            attendance_total += student.attendance

        average = total_average / total if total else 0
        attendance = attendance_total / total if total else 0
        return {
            "total": total,
            "passed": passed,
            "failed": failed,
            "average": average,
            "attendance": attendance,
            "topper": max(self.students, key=lambda s: s.average) if total else None
        }
