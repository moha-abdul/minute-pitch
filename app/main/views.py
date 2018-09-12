from flask import render_template,request,redirect,url_for,abort
from ..models import Role, User
from . import main
from .forms import UpdateProfile,NewPitchForm
from .. import db,photos
from flask_login import login_required, current_user

#views
@main.route('/')
def index():

    '''
    View of root page function that returns the index page and its data
    '''
    return render_template('index.html')

@main.route('/user/<username>')
def profile(username):

    '''
    View of page function that returns the the user's profile
    '''

    user = User.query.filter_by(username = username).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<username>/update',methods = ['GET','POST'])
@login_required
def update_profile(username):
    user = User.query.filter_by(username = username).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',username=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<username>/update/pic',methods= ['POST'])
@login_required
def update_pic(username):
    user = User.query.filter_by(username = username).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',username=username))

@main.route('/pitches')
@login_required
def pitches(pitch_id):

    '''
    View of page function that returns the pitches page and its data
    '''
    # pitches = pitches.query.all()
    return render_template('pitches.html', id = pitch_id, pitch = pitch)


@main.route('/user/<username>/pitch/<int:id>', methods = ['GET','POST'])
@login_required
def new_pitch(id):
    pitch_form = PitchForm()
    pitch = get_pitch(id)
    if form.validate_on_submit():
        title = form.title.data
        pitch = form.pitch.data

        # New pitch instance
        new_pitch = Pitch(pitch_id=pitch.id, pitch_pitches = pitches,pitch_title=title,pitch_posted = time,user=current_user)

        # save pitch method
        new_pitch.save_pitch()
        return redirect(url_for('.pitch',id = pitch.id ))

    title = f'{pitch.title} pitch'
    return render_template('new_pitch.html',title = title, pitch_form=form, pitch=pitch)