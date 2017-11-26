from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField
from wtforms.validators import DataRequired


class EntryForm(FlaskForm):
    """This form is to add/edit fields in the database"""
    title = StringField(
        'Title',
        validators=[
            DataRequired()
        ])

    date = DateField(
        'Date - mm/dd/YYYY',
        format='%m/%d/%Y',
        validators=[
            DataRequired()
        ])

    time_spent = StringField(
        'Time Spent',
        validators=[
            DataRequired()
        ])

    resources_to_remember = TextAreaField(
        'What I Learned',
        validators=[
            DataRequired()
        ])

    what_i_learned = TextAreaField(
        'Resources to Remember',
        validators=[
            DataRequired()
        ])
