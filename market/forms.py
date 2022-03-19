from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired

class RegisterForm(FlaskForm):
  username = StringField(label='User name:', validators=[Length(min=3, max=30), DataRequired()])
  email_address = StringField(label='Email address:', validators=[Email(), DataRequired()])
  password = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
  password_confirm = PasswordField(label='Confirm password:', validators=[EqualTo('password'), DataRequired()])
  submit = SubmitField(label='Create user account')