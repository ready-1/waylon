""" IPAM views"""

from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app

blueprint = Blueprint("ipam", __name__, url_prefix="/ipam", static_folder="../static")

@blueprint.route("/")
def home():
    """Home page."""
    return "Hello World"