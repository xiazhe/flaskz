from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import Required, Length, Regexp
from wtforms import ValidationError
from ..models import Article

class ArticleForm(Form):
    title = StringField('Title', validators=[Required()])
    content = TextAreaField('Content')
    submit = SubmitField('Submit')