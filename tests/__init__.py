from app import init_db
import app

test_app = app.app.test_client()

def teardown():
    pass