from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

class EmailPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])



# class TelephoneForm(FlaskForm):
#     country_code = IntegerField('Country Code', [validators.required()])
#     area_code    = IntegerField('Area Code/Exchange', [validators.required()])
#     number       = StringField('Number')

# class ContactForm(FlaskForm):
#     first_name   = StringField()
#     last_name    = StringField()
#     mobile_phone = FormField(TelephoneForm)
#     office_phone = FormField(TelephoneForm)