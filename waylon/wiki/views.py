# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import login_required, login_user, logout_user

# from waylon.extensions import login_manager
# from waylon.public.forms import LoginForm
# from waylon.user.forms import RegisterForm
# from waylon.user.models import User

from .models import WikiPage
from .forms import WikiPageForm
from waylon.utils import flash_errors

blueprint = Blueprint("wiki", __name__, static_folder="../static", url_prefix="/wiki")



# @login_manager.user_loader
# def load_user(user_id):
#     """Load user by ID."""
#     return User.get_by_id(int(user_id))


@blueprint.route("/list", methods=["GET", "POST"])
def list():
    """Wiki List."""
    pages = WikiPage.query.all()
    return render_template("wiki/list.html", pages=pages)


