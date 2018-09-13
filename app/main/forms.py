from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required
from ..models import Pitch

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself.',validators = [Required()])
    submit = SubmitField('Submit')

class NewPitchForm(FlaskForm):
    title = StringField()
    pitches = TextAreaField('Pitch content', validators=[Required()])
    user_submitting = TextAreaField('posted by', validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    commented = TextAreaField('comment', validators=[Required()])
