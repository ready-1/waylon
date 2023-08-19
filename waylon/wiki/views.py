# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from datetime import datetime as dt

from flask import Blueprint, flash, redirect, render_template, request, url_for
from markdown_it import MarkdownIt

from .forms import WikiPageForm
from .models import WikiPage

blueprint = Blueprint("wiki", __name__, static_folder="../static", url_prefix="/wiki")


# @login_manager.user_loader
# def load_user(user_id):
#     """Load user by ID."""
#     return User.get_by_id(int(user_id))


@blueprint.route("/list", methods=["GET"])
@blueprint.route("/", methods=["GET"])
def list():
    """Wiki List."""
    pages = WikiPage.query.all()
    return render_template("wiki/list.html", pages=pages)


@blueprint.route("/<page_id>", methods=["GET"])
def view_page(page_id):
    md = MarkdownIt("gfm-like", {"linkify": False})
    page = WikiPage.query.filter_by(id=page_id).first()
    html = md.render(page.content)
    print(html)
    print(page.content)
    return render_template("wiki/view.html", page=page, html=html)


@blueprint.route("/new_page", methods=["GET", "POST"])
def new_page():
    """New page."""
    page = WikiPage()
    form = WikiPageForm()
    if request.method == "POST":
        if form.validate_on_submit():
            page.page_name = form.page_name.data
            page.page_title = form.page_title.data
            page.content = form.content.data
            page.last_edit = dt.utcnow()
            page.save()
            flash("Page created.", "success")
            return redirect(url_for("wiki.view_page", page_id=page.id))
    return render_template("wiki/new.html", new_page_form=form, page=page)


@blueprint.route("/edit/<page_id>", methods=["GET", "POST"])
def edit_page(page_id):
    """Edit page."""
    page = WikiPage.query.filter_by(id=page_id).first()
    form = WikiPageForm(obj=page)
    if request.method == "POST":
        # if form.validate_on_submit():
        page.page_name = form.page_name.data
        page.page_title = form.page_title.data
        page.content = form.content.data
        page.last_edit = dt.utcnow()
        page.save()
        flash("Page updated.", "success")
        return redirect(url_for("wiki.list"))
    return render_template("wiki/edit.html", edit_form=form, page=page)


# delete a page
@blueprint.route("/delete/<page_id>", methods=["GET", "POST"])
def delete(page_id):
    """Delete page."""
    page = WikiPage.query.filter_by(id=page_id).first()
    page.delete()
    flash(f"Page {page.page_name} deleted.", "success")
    return redirect(url_for("wiki.list"))
