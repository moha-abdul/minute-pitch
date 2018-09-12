from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

# class LoginForm(FlaskForm):

#     email = StringField('Email title',validators=[Required()])
#     review = TextAreaField('Movie review', validators=[Required()])
#     submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself.',validators = [Required()])
    submit = SubmitField('Submit')

class NewPitchForm(FlaskForm):
    title = StringField()
    pitch = TextAreaField('Pitch content', validators=[Required()])
    submit = SubmitField('Submit')