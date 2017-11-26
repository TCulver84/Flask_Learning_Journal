import datetime

from peewee import *

DATABASE = SqliteDatabase('journal.db')


class Entry(Model):
    """Instantiates and governs datatypes of local instance of database"""
    entered_at = DateTimeField(default=datetime.datetime.now)
    title = CharField()
    date = DateTimeField()
    time_spent = CharField(max_length=100)
    resources_to_remember = TextField()
    what_i_learned = TextField()

    class Meta:
        database = DATABASE

    def initialize(self):
        """Create table and database if they don't already exist"""
        DATABASE.connect()
        DATABASE.create_tables([self], safe=True)
        DATABASE.close()
