from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Category(db.Model):
    '''
    Group class to define the categories for pitches
    '''

    # Name of the table
    __tablename__ = 'category'

    # id column that is the primary key
    id = db.Column(db.Integer, primary_key = True)
    
    # name column for names of categories
    name = db.Column(db.String(255))

    # relationship between group and line class
    lines = db.relationship('Line', backref='category', lazy='dynamic')

    def save_group(self):
        '''
        Function that saves a new category to the groups table
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_groups(cls):
        '''
        Function that queries the Groups Table in the database and returns all the information from the Groups Table
        Returns:
            groups : all the information in the groups table
        '''

        groups = Group.query.all()

        return groups


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    reviews = db.relationship('Review',backref = 'user',lazy = "dynamic")
    votes = db.relationship('Vote', backref='user', lazy='dynamic')


    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'

class Review(db.Model):

    __tablename__ = 'reviews'

    id = db.Column(db.Integer,primary_key = True)
    category_id = db.Column(db.Integer)
    category_title = db.Column(db.String)
    category_review = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))


    def save_review(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_reviews(cls,id):
        reviews = Review.query.filter_by(movie_id=id).all()
        return reviews

    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    
        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)

        return response
