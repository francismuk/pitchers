from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Group,Line,Comment
from .forms import LineForm,CommentForm,GroupForm
from flask_login import login_required,current_user

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home'

    groups = Group.get_groups()

    return render_template('index.html', title = title, groups=groups )

@main.route('/group/new', methods=['GET','POST'])
@login_required
def new_group():

    '''
    View new group route function that returns a page with a form to create a category
    '''

    form = GroupForm()

    if form.validate_on_submit():
        name = form.name.data
        new_group = Group(name=name)
        new_group.save_group()

        return redirect(url_for('.index'))

    title = 'New Group'
    return render_template('new_group.html', group_form = form)


@main.route('/group/<int:id>')
def group(id):

    '''
    View group route function that returns a list of pitches in the route and allows a user to create a pitch for the selected route
    '''
    group = Group.query.get(id)

    if group is None:
        abort(404)

    lines = Line.get_lines(id)
    title = f'{group.name} page'

    return render_template('group.html', title=title, group=group, lines=lines)

@main.route('/group/line/new/<int:id>', methods=['GET','POST'])
@login_required
def new_line(id):

    '''
    View new line route function that returns a page with a form to create a pitch for the specified category
    '''
    group = Group.query.filter_by(id=id).first()

    if group is None:
        abort(404)

    form = LineForm()

    if form.validate_on_submit():
        line_content = form.line_content.data
        new_line = Line( line_content=line_content, group=group, user=current_user)
        new_line.save_line()

        return redirect(url_for('.group', id=group.id ))

    title = 'New Pitch'
    return render_template('new_line.html', title=title, line_form=form)

@main.route('/line/<int:id>')
def single_line(id):

    '''
    View single line function that returns a page containing a pitch, its comments and votes
    '''
    line = Line.query.get(id)
    
    if line is None:
        abort(404)

    comments = Comment.get_comments(id)


    title = f'Pitch {line.id}'

    return render_template('line.html', title=title, line=line, comments=comments)

@main.route('/line/new/<int:id>', methods=['GET','POST'])
@login_required
def new_comment(id):

    '''
    View new line route function that returns a page with a form to create a pitch for the specified category
    '''
    line = Line.query.filter_by(id=id).first()

    if line is None:
        abort(404)

    form = CommentForm()

    if form.validate_on_submit():
        comment_content = form.comment_content.data
        new_comment = Comment( comment_content=comment_content, line=line, user=current_user)
        new_comment.save_comment()

        return redirect(url_for('.single_line', id=line.id ))

    title = 'New Comment'
    return render_template('new_comment.html', title=title, comment_form=form)