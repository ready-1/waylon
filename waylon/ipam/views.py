"""IPAM views."""

from flask import Blueprint, render_template, request, redirect, url_for, flash

from .forms import IPAMForm
from .models import IPAddress

blueprint = Blueprint("ipam", __name__, url_prefix="/ipam", static_folder="../static")

@blueprint.route("/")
def home():
    """Home page."""
    return redirect(url_for("ipam.ip_list"))

@blueprint.route("/list")
def ip_list():
    """IP Address page."""
    ip_addresses = IPAddress.query.all()
    return render_template("ipam/list.html", title="IP Address List", ip_addresses=ip_addresses)

@blueprint.route("/new", methods=["GET", "POST"])
def new():
    """New IP Address."""
    ip = IPAddress()
    form = IPAMForm()
    if request.method == "POST":
        if form.validate_on_submit():
            ip.ipv4_address = form.ipv4_address.data
            ip.ipv4_cidr = form.ipv4_cidr.data
            ip.device = form.device.data
            ip.location = form.location.data
            ip.DHCP = form.DHCP.data
            ip.MAC = form.MAC.data
            ip.save()
            flash("IP Address created.", "success")
            return redirect(url_for("ipam.view", ip_id=ip.id))
        else:
            return render_template("ipam/new.html", title="New IPAM Page", form=form, ip_address=ip)
    return render_template("ipam/new.html", title="New IPAM Page", ipam_form=form, ip_address=ip)

@blueprint.route("/edit", methods=["GET", "POST"])
def edit():
    """New IP Address."""
    ip_id = request.args.get("ip_id")
    ip = IPAddress.query.filter_by(id=ip_id).first()
    form = IPAMForm(obj=ip)
    if request.method == "POST":
        # if form.validate_on_submit(): # TODO: add validation
        ip.ipv4_address = form.ipv4_address.data
        ip.ipv4_cidr = form.ipv4_cidr.data
        ip.device = form.device.data
        ip.location = form.location.data
        ip.DHCP = form.DHCP.data
        ip.MAC = form.MAC.data
        ip.save()
        flash("IP Address updated.", "success")
        return redirect(url_for("ipam.view", ip_id=ip.id))
        # else:
        # return render_template("ipam/edit.html", title=f"Edit {ip.ipv4_address}", ipam_form=form, ip_address=ip)
    return render_template("ipam/edit.html", title=f"Edit {ip.ipv4_address}", ip_id=ip.id, ipam_form=form, ip_address=ip)

@blueprint.route("/view", methods=["GET"])
def view():
    """IP Address page."""
    ip_id = request.args.get("ip_id")
    ip = IPAddress.query.filter_by(id=ip_id).first()
    return render_template("ipam/view.html", title=f"IP Address {ip.ipv4_address}", ip_address=ip)
    

@blueprint.route("/delete")
def delete():
    """Delete IP Address."""
    ip_id = request.args.get("ip_id")
    ip = IPAddress.query.filter_by(id=ip_id).first()
    ip.delete()
    flash(f"IP Address {ip.ipv4_address} deleted.", "success")
    return redirect(url_for("ipam.ip_list"))

