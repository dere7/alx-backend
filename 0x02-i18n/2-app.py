#!/usr/bin/env python3
"""configures flask-babel"""
from flask import Flask, render_template, request
from flask_babel import Babel
from typing import Optional

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
    """selects a languages translation to be used each request"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home() -> str:
    """home displays 'hello world'"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
