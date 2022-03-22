from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User

class RegisterForm(FlaskForm):

  def validate_username(self, username_to_check):
    user = User.query.filter_by(username=username_to_check.data).first()
    if user:
      raise ValidationError(f'Username {username_to_check.data} already exists')

  def validate_email_address(self, email_to_check):
    user = User.query.filter_by(email_address=email_to_check.data).first()
    if user:
      raise ValidationError(f'Username with email address: {email_to_check.data} already exists')

  username = StringField(label='User name:', validators=[Length(min=3, max=30), DataRequired()])
  email_address = StringField(label='Email address:', validators=[Email(), DataRequired()])
  password = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
  password_confirm = PasswordField(label='Confirm password:', validators=[EqualTo('password'), DataRequired()])
  submit = SubmitField(label='Create user account')