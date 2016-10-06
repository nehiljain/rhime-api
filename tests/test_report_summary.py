import json
from nose.tools import eq_
from tests import test_app


def check_content_type(headers):
    eq_(headers['Content-Type'], 'application/json')


def test_reporting_article_summary():
    rv = test_app.get('/reporting/articles/summary')
    check_content_type(rv.headers)
    eq_(rv.status_code, 200)
