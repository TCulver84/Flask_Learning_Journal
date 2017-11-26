from flask import Flask, render_template, redirect, url_for, g, flash

import models
import forms


DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = ' j0o9u4012u43y82h1 3@!#@!321h083h 21oi32'


@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    """Close the database connection after each response."""
    g.db.close()
    return response


@app.route('/')
@app.route('/entries')
@app.route('/entries/')
def entries():
    """Route users to homepage"""
    entries = models.Entry.select().limit(100)
    return render_template('index.html', entries=entries)


@app.route('/entries/add', methods=('GET', 'POST'))
def new_entry():
    """Show new.html, call appropriate form and strip data into database"""
    form = forms.EntryForm()
    if form.validate_on_submit():
        models.Entry.create(title=form.title.data.strip(),
                            date=form.date.data,
                            time_spent=form.time_spent.data.strip(),
                            resources_to_remember=
                                form.resources_to_remember.data.strip(),
                            what_i_learned=form.what_i_learned.data.strip())
        flash("Message posted! Thanks!", "success")
        return redirect(url_for('entries'))
    return render_template('new.html', form=form)


@app.route('/entries/details/<int:entry_id>')
def view_entry(entry_id):
    """Show underlying detail to entries on homepage"""
    entries = models.Entry.select().where(models.Entry.id == entry_id)
    return render_template('detail.html', entries=entries)


@app.route('/entries/edit/<int:entry_id>', methods=('GET', 'POST'))
def edit_entry(entry_id):
    """Prepopulate New Entry form with data from database in
    edit.html template and submit changes to database"""
    entry = models.Entry.get(models.Entry.id == entry_id)
    form = forms.EntryForm(obj=entry)
    if form.validate_on_submit():
        models.Entry.update(title=form.title.data.strip(),
                            date=form.date.data,
                            time_spent=form.time_spent.data.strip(),
                            resources_to_remember=
                                form.resources_to_remember.data.strip(),
                            what_i_learned=
                                form.what_i_learned.data.strip()).where(
                                models.Entry.id == entry_id).execute()
        flash("Message posted! Thanks!", "success")
        return redirect(url_for('entries'))
    return render_template('edit.html', form=form)


@app.route('/entries/delete/<int:entry_id>')
def delete_entry(entry_id):
    """Delete entry from database by clicking on hyperlink"""
    models.Entry.get(models.Entry.id == entry_id).delete_instance()
    return redirect(url_for('entries'))


if __name__ == '__main__':
    try:
        models.Entry().initialize()
    except ValueError:
        pass
    app.run(debug=DEBUG, host=HOST, port=PORT)
