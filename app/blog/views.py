# -*- coding: utf-8 -*
from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response
from flask.ext.login import login_required, current_user
from flask.ext.sqlalchemy import get_debug_queries
from . import blog
from .forms import ArticleForm
from .. import db
from ..models import Permission, Role, User, Article, Post
from ..decorators import admin_required, permission_required

# 请求钩子
@blog.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.ping()
        if not current_user.confirmed \
                and request.endpoint[:5] != 'auth.' \
                and request.endpoint != 'static':
            return redirect(url_for('auth.unconfirmed'))

@blog.route('/', methods=['GET', 'POST'])
@login_required
def index():
    articles = Article.query.all()
    form = ArticleForm()
    if form.validate_on_submit():
        article = Article(title=form.title.data,
                          author=current_user._get_current_object(),
                          content=form.content.data)
        db.session.add(article)
        flash('Your article has been added.')
        return redirect(url_for('blog.index'))

    return render_template('blog/index.html', articles=articles, form=form)

@blog.route('/custom', methods=['GET', 'POST'])
@login_required
def custom():
    articles = Article.query.all()
    form = ArticleForm()
    if request.method == 'POST':
        print form.validate_on_submit()
        print form
    if form.validate_on_submit():
        article = Article(title=form.title.data,
                          author=current_user._get_current_object(),
                          content=form.content.data)
        db.session.add(article)
        flash('Ur article has been added.')
        return redirect(url_for('blog.custom'))

    return render_template('blog/custom_form.html', articles=articles, form=form)