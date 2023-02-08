from app import create_app
from flask import template_rendered
import pytest
from flask.cli import with_appcontext
import click


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('config.py')

    #Creating test client
    with flask_app.test_client() as testing_client:
        yield testing_client


@pytest.fixture
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')