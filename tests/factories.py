# -*- coding: utf-8 -*-
"""Factories to help in tests."""
from datetime import datetime as dt

from factory import Sequence
from factory.alchemy import SQLAlchemyModelFactory

from waylon.database import db
from waylon.ipam.models import IPAddress
from waylon.user.models import User
from waylon.wiki.models import WikiPage


class BaseFactory(SQLAlchemyModelFactory):
    """Base factory."""

    class Meta:
        """Factory configuration."""

        abstract = True
        sqlalchemy_session = db.session


class UserFactory(BaseFactory):
    """User factory."""

    username = Sequence(lambda n: f"user{n}")
    email = Sequence(lambda n: f"user{n}@example.com")
    active = True

    class Meta:
        """Factory configuration."""

        model = User


class WikiFactory(BaseFactory):
    """User factory."""

    page_name = Sequence(lambda n: f"page{n}")
    page_title = Sequence(lambda n: f"Page {n}")
    content = Sequence(lambda n: f"This is page {n}")
    last_edit = dt.utcnow()

    class Meta:
        """Factory configuration."""

        model = WikiPage

class IPAddressFactory(BaseFactory):
    """IP Address factory."""

    ipv4_address = Sequence(lambda n: f"192.168.251.{n}")
    ipv4_cidr = Sequence(lambda n: f"{n}")
    device = Sequence(lambda n: f"Device Number {n}")
    location = Sequence(lambda n: f"Location Number{n}")
    DHCP = True
    MAC = Sequence(lambda n: f"99:99:99:99:99:{n}")


    class Meta:
        """Factory configuration."""

        model = IPAddress