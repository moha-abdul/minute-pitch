from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitches = db.relationship('Pitch',backref = 'user',lazy = "dynamic")
    # comment = db.relationship('Comment',backref = 'user',lazy = "dynamic")

    def __repr__(self):
        return f'User {self.username}'

    pass_secure  = db.Column(db.String(255))

    @property
    def password(self):
        '''
        blocks access to the password property
        '''
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        '''
        takes in password, hashes it and compares it to the hashed password
        '''
        return check_password_hash(self.pass_secure,password)

    
    '''
    @login_manage.user_loader that modifies the load_user function by passing in a user_id to the function that queries the database and gets a User with that ID
    '''
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    pitches = db.Column(db.String(255))
    title = db.Column(db.String(255))
    comment = db.Column(db.String(255))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    # vote = vote.Column(db.Integer)
    # comment = db.relationship('Comment',backref = 'pitch',lazy = "dynamic")


    def save_pitch(self):
        '''
        this method will save the instance of the pitch model to the session and commit it to the database
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(id):
        pitches = Pitch.query.filter_by(id = id).all()
        return pitches

    @classmethod
    def get_pitch(cls,id):
        '''
        class method will take in a pitch id and retrieve that reviews for that pitch
        '''
        pitches = Pitch.query.filter_by(pitch_id=id).all()
        return pitches

class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    post_comment = db.Column(db.String(255), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    blogs = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    time = db.Column(db.DateTime, default=datetime.utcnow)

    def save_comment(self):
        '''
        Save comments
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, id):
        comments = Comment.query.filter_by(id=id).all()
        return comments
