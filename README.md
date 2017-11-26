Synopsis

Create a local web interface of a learning journal. The main (index) page will list journal entry titles and dates. Each journal entry title will link to a detail page that displays the title, date, time spent, what you learned, and resources to remember. Include the ability to add or edit journal entries. When adding or editing a journal entry, there must be prompts for title, date, time spent, what you learned, resources to remember. The results for these entries must be stored in a database and displayed in a blog style website. The HTML/CSS for this site has been supplied for you.

Code Example

The code library contains 1 application (app.py) that refers to a database model in models.py and form structure in forms.py.

The application uses the flask framework to route the user between index.html, new.html, edit.html, and detail.html -> a file macros.html is used to reduce the amount of repeatable code in the file.

For Example - in app.py

1. Flask is used to route the user to /entries/add
2. forms.py is called in forms.EntryForm() to associate the object with a variable
3. models.Entry.create takes the data within the EntryForm() and posts it to the peewee database

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


Motivation

The motivation for this project was to be able to build a website that speaks to a database within the flask framework to fully understand the coding skills needed to be a full stack Python web developer.


Installation

To install the project download all files to a location of your choosing on your computer, log into the terminal (on a MAC) and instantiate the program from the directory where you stored the files as follows:

    python3 -i app.py

From there, log into your browser and navigate accordingly


Tests

To test this application navigate to each hyperlink within the browser, add a log, edit a log, and test a log.


Contributors

This project was inspired by the teachers at teamtreehouse.com and was developed by Taylor.


License

Opensource for your enjoyment!