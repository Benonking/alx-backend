#!/usr/bin/env python3
'''
A basic flask app
'''
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config:
    '''
    config class to store avalable languages and time zone defaults
    '''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)
app.url_map.strict_slashes = False


@app.route("/", strict_slashes=False)
def hello() -> str:
    '''index page'''
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
