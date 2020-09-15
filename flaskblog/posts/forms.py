from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()], render_kw={"placeholder": "Enter the title for new post"})
    content = TextAreaField('Content', validators=[DataRequired()], render_kw={"placeholder": "Enter your post here"})
    submit = SubmitField('Post')
