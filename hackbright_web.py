"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/new-student")
def add_student_form():
    """Show form for adding a new student."""

    return render_template("student_add.html")


@app.route("/student_add", methods=['POST'])
def student_add():
    """Add a student."""

    first=request.form.get('first')
    last=request.form.get('last')
    github=request.form.get('github')
    hackbright.make_new_student(first, last, github)

    return render_template("confirmation.html", jinja_github=github)



@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    rows = hackbright.get_grades_by_github(github)
    first, last, github = hackbright.get_student_by_github(github)

    html = render_template("student_info.html",
                           rows=rows,
                           github=github,
                           first=first,
                           last=last)

    return html


@app.route("/student-search")
def get_student_form():
    """ Show form for searching for a student."""

    return render_template("student_search.html")


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
