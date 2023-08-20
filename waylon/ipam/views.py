"""IPAM views."""

from flask import Blueprint, render_template

blueprint = Blueprint("ipam", __name__, url_prefix="/ipam", static_folder="../static")

@blueprint.route("/")
def home():
    """Home page."""
    return render_template("ipam/list.html", title="IPAM")
