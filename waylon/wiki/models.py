# -*- coding: utf-8 -*-
"""Wiki models."""
from datetime import datetime as dt

from waylon.database import Column, CRUDMixin, PkModel, db


class WikiPage(PkModel, CRUDMixin):
    """A wiki page."""

    __tablename__ = "wikis"

    page_name = Column(db.String(80), unique=True, nullable=False)
    page_title = Column(db.String(80), unique=True, nullable=False)
    content = Column(db.Text, nullable=False)
    last_edit = dt.utcnow()

    # def save(self):
    #     """
    #     Save oneself.
    #     """
    #     with db.session.begin():
    #         db.session.add(self)

    def __repr__(self):
        """Represent instance as a unique string."""
        return f"<WikiPage({self.page_name!r})>"
