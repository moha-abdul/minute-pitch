from flask import render_template,request,redirect,url_for,abort,flash
from ..models import Role, User,Pitch
from . import main
from .forms import UpdateProfile,NewPitchForm,CommentForm
from .. import db,photos
from flask_login import login_required, current_user

#views
@main.route('/')
def index():

    '''
    View of root page function that returns the index page and its data
    '''
    return render_template('index.html')

@main.route('/all_pitches')
@login_required
def all_pitches():
    pitches=Pitch.query.all()
    return render_template('all_pitches.html', pitches = pitches)

@main.route('/new_pitch',methods=['GET','POST'])
@login_required
def new_pitch():
    form=NewPitchForm()
    if form.validate_on_submit():
        pitches=Pitch(title=form.title.data,pitches=form.pitches.data)
        db.session.add(pitches)
        db.session.commit()
        flash('your pitch, created!')
        return redirect(url_for('main.all_pitches'))

    pitches=Pitch.query.all()
    return render_template('all_pitches.html',pitch = pitches)

# @main.route('/new_pitch/<int:id>')
# @login_required
# def single_pitch(pitch):
#     pitch = Pitch.query.get(pitch)
#     return render_template('single_pitch.html',pitch = pitch)
    
    
    

# @main.route('/single_pitch/new_comment',methods=['GET','POST'])
# @login_required
# def new_pitch():
#     form = CommentForm()
#     if form.validate_on_submit():
#         db.session.add(comment)
#         db.session.commit()
#         flash('your comment, also created!')
#         return redirect(url_for('main.single_pitch'))

    # comments = Comment.query.all()
    # pitches = Pitch.query.filter_by(id = id).first()
    # return render_template('new_comment.html',form=form,pitches=pitches, comments = comments)

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

