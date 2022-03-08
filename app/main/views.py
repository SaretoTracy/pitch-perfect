from flask import render_template
from . import main

# Views


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    heading = "Pitch-Perfect"
    return render_template('index.html', head=heading)


@main.route('/error')
def error():

    return render_template('error.html')
