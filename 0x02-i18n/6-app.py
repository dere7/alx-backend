#!/usr/bin/env python3
"""configures flask-babel"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Optional, Mapping

app = Flask(__name__)
babel = Babel(app)


class Config:
    """conifguration for app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> Optional[str]:
    """selects a languages translation to be used for each request"""

    # locale from url parameters
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return request.args['locale']

    # locale from user setting
    user = getattr(g, 'user', None)
    if user and user.get('locale') in app.config['LANGUAGES']:
        return user.get('locale')

    # locale from request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Optional[Mapping]:
    """returns user dictionary"""
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """gets user before each request"""
    user = get_user()
    if user:
        g.user = user


@app.route('/')
def home() -> str:
    """home displays 'hello world'"""
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run()
