from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField, DateField
from wtforms.validators import Length, Email, DataRequired, url


class MyForm(FlaskForm):
    name = StringField(label="Name")
    email = StringField(label='Email', validators=[Email(message="Please provide a valid email")])
    phone = StringField(label="Phone", validators=[Length(min=10, message="Please put in a valid number")])
    description = StringField(label="Reason for Enquiry")
    submit = SubmitField(label="Submit")

class work_form(FlaskForm):
    job_title = StringField(label="Job Title", validators=[DataRequired(message="Please enter a Job Title")])
    start_time = StringField(label="Start Month and Year")
    end_time = StringField(label="End Month and Year")
    company = StringField(label="Company Name", validators=[DataRequired(message="Please enter a Company name")])
    job_description = StringField(label="Job Description", validators=[DataRequired(message="Please enter the Main Role "
                                                                                            "of your Position ")])
    job_description1 = StringField(label="Job Description", validators=[DataRequired(message="Please enter the Next Main "
                                                                                            " Role of your Position")])
    job_description2 = StringField(label="Job Description", validators=[DataRequired(message="Please enter a the Final "
                                                                                            "Role of your Position")])
    job_image = StringField(label="Image URL", validators=[DataRequired(message="Please enter a image URL")])
    job_url = StringField(label="Website URL", validators=[url(require_tld=True, message="Please enter a image URL")])
    submit = SubmitField(label="Submit")