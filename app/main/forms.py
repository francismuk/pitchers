from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class GroupForm(FlaskForm):
    '''
    Class to create a wtf form for creating a pitch
    '''
    name =  StringField('Category Name', validators=[Required()])
    submit = SubmitField('Create')

class LineForm(FlaskForm):
    '''
    Class to create a wtf form for creating a pitch
    '''
    line_content =  StringField('One Minute Pitch', validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    '''
    Class to create a wtf form for creating a feedback on a pitch
    '''
    comment_content =  TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Submit')