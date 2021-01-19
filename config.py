import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
# clod database elephantsql.com
SQLALCHEMY_DATABASE_URI = 'postgres://wbmwctrt:DQiMTH5iHLL6JZqqdEcdzPkf1aG7WYAv@ruby.db.elephantsql.com:5432/wbmwctrt'


# TODO IMPLEMENT DATABASE URL
# SQLALCHEMY_DATABASE_URI = 'postgres://awotefalharbi@localhost:5432/fyyur1'
# SQLALCHEMY_TRACK_MODIFICATIONS = False