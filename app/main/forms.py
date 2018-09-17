from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required
from ..models import Pitch

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself.',validators = [Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    title = StringField()
    body = TextAreaField('Pitch content', validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    commented = TextAreaField('comment', validators=[Required()])
