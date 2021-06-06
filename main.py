import smtplib
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from form import MyForm, work_form
import requests

# Create Server
app = Flask(__name__)
Bootstrap(app)
app.secret_key = "some secret string"

# Create DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mycvwebsite2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CREATE TABLE
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(250), unique=True, nullable=False)
    start_job = db.Column(db.String(250), nullable=False)
    end_job = db.Column(db.String(250))
    company = db.Column(db.String(500), nullable=False)
    job_description = db.Column(db.String(500), nullable=False)
    job_description1 = db.Column(db.String(500), nullable=False)
    job_description2 = db.Column(db.String(500), nullable=False)
    job_image = db.Column(db.String(2000), nullable=False)
    job_url = db.Column(db.String(2000), nullable=False)


db.create_all()

my_email = "cairns.python@gmail.com"
password = "Lionheart93"

email_to = "cairns.python@gmail.com"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/education")
def education():
    return render_template("education.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = MyForm()
    if form.validate_on_submit():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()  # makes connection secure
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=email_to,
                                msg=f"Subject:New Contact\n\nName: {request.form['name']}"
                                    f"\n Email: {request.form['email']}"
                                    f"\n Phone: {request.form['phone']}"
                                    f"\n Description: {request.form['description']}".encode("utf8"))
        return redirect(url_for('home'))
    return render_template("contact.html", form=form)


@app.route("/experience", methods=["GET", "POST"])
def experience():
    all_jobs = Job.query.order_by(Job.job_title).all()
    for i in range(len(all_jobs)):
        all_jobs[i].ranking = len(all_jobs) - i
    db.session.commit()
    return render_template("experience.html", jobs=all_jobs)


@app.route("/addwork", methods=["GET", "POST"])
def add_work():
    form = work_form()
    if form.validate_on_submit():
        job_title = request.form["job_title"]
        start_job = request.form["start_time"]
        end_job = request.form["end_time"]
        company = request.form["company"]
        job_description = request.form["job_description"]
        job_description1 = request.form["job_description1"]
        job_description2 = request.form["job_description2"]
        job_image = request.form["job_image"]
        job_url = request.form["job_url"]
        new_job = Job(
            job_title=str(job_title),
            start_job=str(start_job),
            end_job=str(end_job),
            company=str(company),
            job_description=str(job_description),
            job_description1=str(job_description1),
            job_description2=str(job_description2),
            job_image=str(job_image),
            job_url=str(job_url)
        )
        db.session.add(new_job)
        db.session.commit()
        return redirect(url_for('experience'))
    return render_template("addwork.html", form=form, job=Job)


@app.route("/projects")
def projects():
    return render_template("projects.html")


if __name__ == '__main__':
    app.run(debug=True)
