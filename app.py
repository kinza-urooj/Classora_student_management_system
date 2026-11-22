from flask import Flask, render_template, request, redirect, url_for, flash, Response
import csv
import io
from student_manager import StudentManager

app = Flask(__name__)
app.secret_key = "edutrack-demo-key"
manager = StudentManager()

@app.route("/")
def dashboard():
    students = manager.get_all()
    stats = manager.get_stats()
    return render_template("index.html", students=students, stats=stats)

@app.route("/add", methods=["POST"])
def add_student():
    try:
        name = request.form["name"].strip()
        roll_no = request.form["roll_no"].strip()
        python = float(request.form["python"])
        math = float(request.form["math"])
        english = float(request.form["english"])
        attendance = float(request.form["attendance"])

        if not name or not roll_no:
            flash("Please enter student name and roll number.", "error")
        elif any(s.roll_no == roll_no for s in manager.get_all()):
            flash("That roll number already exists.", "error")
        elif not all(0 <= mark <= 100 for mark in [python, math, english, attendance]):
            flash("Marks and attendance must be between 0 and 100.", "error")
        else:
            student = Student(name, roll_no, python, math, english, attendance)
            manager.add(student)
            flash(f"{name} added successfully!", "success")
    except ValueError:
        flash("Please enter valid numbers for marks and attendance.", "error")
    return redirect(url_for("dashboard"))

@app.route("/delete/<roll_no>", methods=["POST"])
def delete_student(roll_no):
    if manager.delete(roll_no):
        flash("Student deleted.", "success")
    else:
        flash("Student not found.", "error")
    return redirect(url_for("dashboard"))

@app.route("/search")
def search():
    term = request.args.get("q", "").strip().lower()
    students = manager.get_all()
    results = [s for s in students if term in s.name.lower() or term in s.roll_no.lower()]
    return render_template("index.html", students=results, stats=manager.get_stats(), search_term=term)

@app.route("/export")
def export_csv():
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Name", "Roll Number", "Average", "Grade", "Attendance", "Status"])
    for student in manager.get_all():
        writer.writerow([student.name, student.roll_no, f"{student.average:.2f}", student.grade, f"{student.attendance:.1f}%", student.status])
    return Response(output.getvalue(), mimetype="text/csv", headers={"Content-Disposition":"attachment; filename=student_report.csv"})

from student import Student

if __name__ == "__main__":
    app.run(debug=True)
