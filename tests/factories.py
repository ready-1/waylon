# -*- coding: utf-8 -*-
"""Factories to help in tests."""
from factory import Sequence
from factory.alchemy import SQLAlchemyModelFactory

from waylon.database import db
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
    last_edit = db.DateTime.utcnow

    class Meta:
        """Factory configuration."""

        model = WikiPage
