from wtforms import StringField, PasswordField, BooleanField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.widgets import TextArea


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember = BooleanField('Remember')


class RegisterForm(FlaskForm):

    email = StringField('Email', validators=[InputRequired(), Email()])
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class PitchForm(FlaskForm):

    title = StringField('Title of pitch', validators=[InputRequired()])
    category = SelectField(u'Select Pitch Category', choices=[('....Select Category', 'Select Category.....'), (
        'Product', 'Product'), ('Business', 'Business'), ('Elevator', 'Elevator'), ('Innovative', 'Innovative'), ('Pickup lines', 'Pickup lines'), ('Interview', 'Interview')])
    description = StringField(
        'Pitch', validators=[InputRequired()], widget=TextArea())


class CommentForm(FlaskForm):
    content = StringField('Comment')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[InputRequired()])
    submit = SubmitField('Submit')
