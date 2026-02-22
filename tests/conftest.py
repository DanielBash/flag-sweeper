"""- Tests common context"""

# -- importing modules
import pytest, sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import main


# - app
@pytest.fixture()
def app():
    app = main.app
    app.config.update({"TESTING": True})
    yield app


# - app client
@pytest.fixture()
def client(app):
    return app.test_client()
