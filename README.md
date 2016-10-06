# rhime-api



TODO:
- add a mock database dump or url creds to a mongo instance for testing
- add nose test cases https://github.com/kelsmj/flask-test-example.
- create runnosetest.sh
- setup travis ci/circle ci for testing
- containerise the application


POST to /reporting/articles/summary
{
  "report_request": {
    "user_id":"selvam4@test.com",
    "date_ranges":[
      {
        "start_date":"2015-06-15",
        "end_date":"2015-06-30"
      }]
  }
}


RESPONSE:

{
    user_id: "selvam4@test.com"
    report: [
        {
            start_date:"2015-06-15",
            end_data:"2015-06-30",
            archived_count: 14,
            added_count: 40,
            deleted_count: 30
            archived_time_sum: 3000,
            added_time_sum; 2400,
        }

    ]
}















