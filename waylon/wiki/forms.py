# -*- coding: utf-8 -*-
"""User forms."""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

from .models import WikiPage


class WikiPageForm(FlaskForm):
    """Wiki page form."""

    page_name = StringField("Page name", validators=[DataRequired()])
    page_title = StringField("Page title", validators=[DataRequired()])
    content = StringField("Content", widget=TextArea())
    last_edit = DateField("Last edit")
    submit = SubmitField("Save")


    # def __init__(self, *args, **kwargs):
    #     """Create instance."""
    #     super(WikiPageForm, self).__init__(*args, **kwargs)
    #     self.page_name = ""
    #     self.page_title = ""
    #     self.content = ""
    #     self.last_edit = ""

    def validate(self, **kwargs):
        """Validate the form."""
        initial_validation = super(WikiPageForm, self).validate()
        if not initial_validation:
            return False
        page = WikiPage.query.filter_by(page_name=self.page_name.data).first()
        if page:
            self.page_name.errors.append("Page name already exists")
            return False
        page = WikiPage.query.filter_by(page_title=self.page_title.data).first()
        if page:
            self.page_title.errors.append("Page Title already registered")
            return False
        return True
