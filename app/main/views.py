from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Review, User, Category
from .forms import ReviewForm, UpdateProfile
from flask_login import login_required,current_user

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Welcome to the best Pitching Webiste'

    categories = Category.get_category()

    return render_template('index.html', title = title, categories=categories )

@main.route('/category/new', methods=['GET','POST'])
@login_required
def new_group():

    '''
    View new group route function that returns a page with a form to create a category
    '''

    form = CategoryForm()

    if form.validate_on_submit():
        name = form.name.data
        new_category = Category(name=name)
        new_category.save_category()

        return redirect(url_for('.index'))

    title = 'New Category'
    return render_template('new_category.html', category_form = form)


@main.route('/category/<int:id>')
def category(id):

    '''
    View category route function that returns a list of pitches in the route and allows a user to create a pitch for the selected route
    '''
    category = Category.query.get(id)

    if category is None:
        abort(404)

    lines = Line.get_lines(id)
    title = f'{category.name} page'

    return render_template('category.html', title=title, category=category, lines=lines)

@main.route('/category/line/new/<int:id>', methods=['GET','POST'])
@login_required
def new_line(id):

    '''
    View new line route function that returns a page with a form to create a pitch for the specified category
    '''
    category = Category.query.filter_by(id=id).first()

    if category is None:
        abort(404)

    form = LineForm()

    if form.validate_on_submit():
        line_content = form.line_content.data
        new_line = Line( line_content=line_content, category=category, user=current_user)
        new_line.save_line()

        return redirect(url_for('.category', id=category.id ))

    title = 'New Pitch'
    return render_template('new_pitch.html', title=title, line_form=form)

@main.route('/line/<int:id>')
def single_line(id):

    '''
    View single line function that returns a page containing a pitch, its comments and votes
    '''
    line = Line.query.get(id)
    
    if line is None:
        abort(404)

    comments = Comment.get_comments(id)

    # vote = Vote.query.all()

    total_votes = Vote.num_vote(line.id)

    title = f'Pitch {line.id}'

    return render_template('line.html', title=title, line=line, comments=comments, total_votes=total_votes)

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

@main.route('/line/upvote/<int:id>')
@login_required
def upvote(id):

    '''
    View function that add one to the vote_number column in the votes table
    '''
    line = Line.query.get(id)

    new_vote = Vote(user=current_user, line=line, vote_number=1)
    new_vote.save_vote()
    return redirect(url_for('.single_line', id=line.id))


@main.route('/line/downvote/<int:id>')
@login_required
def downvote(id):

    '''
    View function that add one to the vote_number column in the votes table
    '''
    line = Line.query.filter_by(id=id).first()
    
    new_vote = Vote(user=current_user, line=line, vote_number= -1)
    new_vote.save_vote()
    return redirect(url_for('.single_line', id=line.id))