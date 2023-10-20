"""Flask routes."""
from flask import render_template
from flask import current_app as app
from .api import fetch_numerals


@app.route('/', methods=['GET'])
def home():
    """Homepage."""
    return render_template(
        'index.html',
        title='Example home page',
    )


@app.route('/about', methods=['GET'])
def about():
    """About page."""
    numerals = fetch_numerals(app)
    return render_template(
        'about.html',
        title='Example about page',
        numerals=numerals
    )
