#!/usr/bin/env python3
'''
A basic flask app
'''
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union
import flask

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


@babel.localeselector
def get_locale() -> str:
    '''retrieve locale for web page'''
    queries = request.query_string.decode('utf-8').split('&')
    query_table = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        queries,
    ))
    if 'locale' in query_table:
        if query_table['locale'] in app.config["LANGUAGES"]:
            return query_table['locale']
    return request.accept_languages.best_match(Config.LANGUAGES)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    '''retrive a user '''
    id = request.args.get('login_as')
    if id:
        return users.get(int(id))
    return None


@app.before_request
def before_request() -> None:
    '''set user before request'''
    g.user = get_user()


@app.route("/", strict_slashes=False)
def hello() -> str:
    '''index page'''
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run()
