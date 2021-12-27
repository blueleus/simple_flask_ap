import click
from flask import Flask
from app.users import users
from flask.cli import with_appcontext
import os
import unittest


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object('config.Config')
    else:
        # load the test config if passed in
        app.config.from_object(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialize database
    from app.models import db
    db.init_app(app)

    # Add commands
    app.cli.add_command(test)

    # Add blueprints
    app.register_blueprint(users)

    return app


@click.command()
@with_appcontext
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)
