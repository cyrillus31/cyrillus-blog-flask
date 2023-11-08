from flask_wtf import FlaskForm
from wtform import StringField, PasswordField, SubmitField, BooleanField
from wtform.validators import DataRequired, Length, EqualTo, Email 


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = StringField('Password',
                           validators=[DataRequired()])
    password_confirm = StringField('Password confirmation',
                                   validators=[DataRequired(), EqualTo('password')])
    submit_button = SubmitField('SIGN IN')   


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = StringField('Password',
                           validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit_button = SubmitField('LOGIN')

