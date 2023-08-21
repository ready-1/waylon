"""IPAM forms."""
import re

from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, IPAddress


# TODO: add validators for IPv4 and CIDR

# def valididate_ipv4():
#     """Validate IPv4."""
#     message = "Invalid IPv4 address."

#     def _validate_ipv4(form, field):
#         """Validate IPv4."""
#         if not re.match(
#             "^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",
#             field.data,
#         ):
#             raise ValueError(message)


# def valididate_cidr():
#     """Validate CIDR."""
#     message = "Invalid CIDR."

#     def _validate_cidr(form, field):
#         """Validate CIDR."""
#         if not 1 <= int(field.data) <= 32:
#             raise ValueError(message)

#     return _validate_cidr


# def validate_mac():
#     """Validate MAC."""
#     message = "Invalid MAC. Must be in the format ab:cd:ef:12:34:56."

#     def _validate_mac(form, field):
#         """Validate MAC."""
#         if re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac.lower()):
#             raise ValueError(message)

#     return _validate_mac


class IPAMForm(FlaskForm):
    """IPAM form."""

    ipv4_address = StringField(
        "IPv4 address", validators=[DataRequired(), Length(min=7, max=15), IPAddress()]
    )
    ipv4_cidr = StringField(
        "IPv4 CIDR", validators=[DataRequired(), Length(min=1, max=2)]
    )
    device = StringField("Device", validators=[DataRequired(), Length(min=1, max=80)])
    location = StringField(
        "Location", validators=[DataRequired(), Length(min=1, max=80)]
    )
    DHCP = BooleanField("DHCP")
    MAC = StringField("MAC", validators=[DataRequired(), Length(min=1, max=17)])
    submit = SubmitField("Submit")
