# -*- coding: utf-8 -*
from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response
from flask.ext.login import login_required, current_user
from flask.ext.sqlalchemy import get_debug_queries
from . import blog
# from .forms import
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
def index():
    articles = Post.query.all()
    return render_template('blog/index.html', articles=articles)