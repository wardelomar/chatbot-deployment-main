from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    phone = StringField("phone", validators=[DataRequired()])
    personal = SelectField("personal", choices=["1 personal","2 personal","3 personal","4 personal","5 personal","6 personal","7 personal"])
    date = StringField("date", validators=[DataRequired()])
    time = SelectField("time", choices=["08:00am","09:00am","10:00am","11:00am","12:00am","01:00pm","02:00pm","03:00pm","04:00pm","05:00pm","06:00pm","07:00pm","08:00pm","09:00pm","10:00pm"])
    message = TextAreaField("message", validators=[DataRequired()])
    submit = SubmitField("add")


