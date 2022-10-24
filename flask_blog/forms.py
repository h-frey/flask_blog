
from flask_wtf import Form
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField,validators
from wtforms.validators import InputRequired,Email,ValidationError
from flask_blog.models import User


class RegistrationForm(Form):
    username = StringField("Username", [InputRequired("Please enter your name")])
    email = StringField("Email",[InputRequired("Please enter your email adress"),Email("This field requires a valid email adress ")])
    password = PasswordField("Password", [InputRequired()])
    confirm_password = PasswordField("Confirm Password", [InputRequired(),validators.EqualTo("password",message="Passwords must match")])
    submit = SubmitField("Sign Up")

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if  user:
            raise ValidationError("That username is taken,please use another one")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                "That email is taken,please use another one")

class LoginForm(Form):
    
    email = StringField("Email", [InputRequired("Please enter your name")])

    password = PasswordField("Password", [InputRequired("Please enter your name")])

    remember = BooleanField("Remember Me")

    submit = SubmitField("Login")


class UpdateAccountForm(Form):
    username = StringField(
        "Username", [InputRequired("Please enter your name")])
    email = StringField("Email", [InputRequired("Please enter your email adress"), Email(
        "This field requires a valid email adress ")])
    image_file = FileField("Update Profile Picture",validators=[FileAllowed(["jpg","png"])])
    submit = SubmitField("Update")

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                    "That username is taken,please use another one")

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    "That email is taken,please use another one")

class PostForm(Form):
    title = StringField("Title",validators = [InputRequired()])
    content = TextAreaField("Content", [InputRequired()])
    submit = SubmitField("Post")

class RequestResetForm(Form):
    email = StringField("Email", [InputRequired("Please enter your email")])
    submit = SubmitField("Request Password Reset")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError(
                 "There is no account with that email address. You must regsiter your account first.")

class ResetPasswordForm(Form):
    password = PasswordField("Password", [InputRequired()])
    confirm_password = PasswordField("Confirm Password", [InputRequired(),validators.EqualTo("password",message="Passwords must match")])
    submit = SubmitField("Reset Password")
