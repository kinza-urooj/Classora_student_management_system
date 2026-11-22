class Student:
    """Stores one student's information and calculates academic results."""

    def __init__(self, name, roll_no, python, math, english, attendance):
        self.name = name
        self.roll_no = roll_no
        self.python = python
        self.math = math
        self.english = english
        self.attendance = attendance

    @property
    def average(self):
        return (self.python + self.math + self.english) / 3

    @property
    def grade(self):
        if self.average >= 80:
            return "A"
        elif self.average >= 70:
            return "B"
        elif self.average >= 60:
            return "C"
        elif self.average >= 50:
            return "D"
        return "F"

    @property
    def status(self):
        if self.average >= 50:
            return "Pass"
        return "Fail"

    def to_dict(self):
        return {
            "name": self.name,
            "roll_no": self.roll_no,
            "python": self.python,
            "math": self.math,
            "english": self.english,
            "attendance": self.attendance
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["roll_no"], data["python"], data["math"],
                   data["english"], data["attendance"])
