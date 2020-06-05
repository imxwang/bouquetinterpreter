"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import request
from flask import render_template
from flaskexample import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )


@app.route('/imgurl', methods=['POST'])
def imgurl():
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        imgpath=request.form['imgURL']
    )