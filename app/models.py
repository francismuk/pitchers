from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from sqlalchemy.sql import func

@login_manager.user_loader
def load_user(user_id):
    '''
    @login_manager.user_loader Passes in a user_id to this function
    Function queries the database and gets a user's id as a response
    '''
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    '''
    User class to define a user in the database
    '''

    # Name of the table
    __tablename__ = 'users'

    # id column that is the primary key
    id = db.Column(db.Integer, primary_key = True)

    # username column for usernames
    username = db.Column(db.String(255))

    # email column for a user's email address
    email = db.Column(db.String(255), unique = True, index = True)

    # password_hash column for passwords
    password_hash = db.Column(db.String(255))

    # relationship between user and line class
    lines = db.relationship('Line', backref='user', lazy='dynamic')

    # relationship between user and comment class
    comments = db.relationship('Comment', backref='user', lazy='dynamic')

    # relationship between line and comment class

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)


    def __repr__(self):
        return f'User {self.username}'



class Group(db.Model):
    '''
    Group class to define the categories for pitches
    '''

    # Name of the table
    __tablename__ = 'groups'

    # id column that is the primary key
    id = db.Column(db.Integer, primary_key = True)
    
    # name column for names of categories
    name = db.Column(db.String(255))

    # relationship between group and line class
    lines = db.relationship('Line', backref='group', lazy='dynamic')

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


class Line(db.Model):
    '''
    Line class to define the pitches
    '''

    # Name of the table
    __tablename__ = 'lines'

    # id column that is the primary key
    id = db.Column(db.Integer, primary_key = True)

    # line_content column for the one minute pitch a user writes
    line_content = db.Column(db.String(200))

    # group_id column for linking a line to a specific group
    group_id = db.Column(db.Integer, db.ForeignKey("groups.id") )

    # user_id column for linking a line to a specific group
    user_id = db.Column(db.Integer, db.ForeignKey("users.id") )

    # relationship between line and comment class
    comments = db.relationship('Comment', backref='line', lazy='dynamic')

    # relationship between line and comment class

    def save_line(self):
        '''
        Function that saves a new pitch to the lines table
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_lines(cls,group_id):
        '''
        Function that queries the Lines Table in the database and returns only information with the specified group id
        Args:
            group_id : specific group_id
        Returns:
            lines : all the information for lines with the specific group id 
        '''
        lines = Line.query.order_by(Line.id.desc()).filter_by(group_id=group_id).all()

        return lines

class Comment(db.Model):
    '''
    Comment class to define the feedback from users
    '''

    # Name of the table
    __tablename__ = 'comments'

    # id column that is the primary key
    id = db.Column(db.Integer, primary_key = True)

    # comment_content for the feedback a user gives toa pitch
    comment_content = db.Column(db.String)

    # line_id column for linking a line to a specific line
    line_id = db.Column(db.Integer, db.ForeignKey("lines.id") )

    # user_id column for linking a line to a specific group
    user_id = db.Column(db.Integer, db.ForeignKey("users.id") )

    def save_comment(self):
        '''
        Function that saves a new comment given as feedback to a pitch
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,line_id):
        '''
        Function that queries the Comments Table in the database and returns only information with the specified line id
        Args:
            line_id : specific line_id
        Returns:
            comments : all the information for comments with the specific line id 
        '''
        comments = Comment.query.filter_by(line_id=line_id).all()

        return comments