import json
from nose.tools import eq_
from tests import test_app


def check_content_type(headers):
    eq_(headers['Content-Type'], 'application/json')


def test_reporting_article_summary():
	d = dict(
				report_request=dict(
			    	user_id="selvam4@test.com",
			    	date_ranges=[
			        	dict(start_date="2015-06-15",end_date="2015-06-25")
			    	]
			    ) 
			)
	print(d)
    rv = test_app.post('/reporting/articles/summary', data=d)
    check_content_type(rv.headers)
    eq_(rv.status_code, 200)

    resp = json.loads(rv.data)
    eq_(resp['user_id'], "selvam4@test.com")
    assert len(resp['report']) > 0 
