umapi_client
============

Client wrapper for Wikipedia User Metrics API.

See https://github.com/wikimedia/user_metrics for UMAPI implementation.

Usage
-----

Set the ``UMAPI_USER`` and ``UMAPI_PASS`` in ``umapi_client/config.py``
(copied from ``umapi_client/config.py.settings``).  Ensure that
``call_client`` is executable and requests are invoked by simply
calling this script followed by the URL path and parameters of a request. Only
cached responses will return a response with JSON, otherwise the request will
be queued by the service.


    RFaulkner-WMF:umapi_client rfaulkner$ cd umapi_client/
    RFaulkner-WMF:umapi_client rfaulkner$ ./scripts/call_client "cohorts/\
    ryan_test_2/bytes_added"
    {
      "cohort": "ryan_test_2",
      "group": "default",
      "cohort_last_generated": "2013-03-19 07:43:26",
      "aggregator": "None",
      "metric": "bytes_added",
      "namespace": [
        0
      ],
      "project": "enwiki",
      "time_of_response": "2013-03-19 07:43:32",
      "datetime_start": "2010-10-25 08:00:00",
      "datetime_end": "2011-01-01 00:00:00",
      "header": [
        "user_id",
        "bytes_added_net",
        "bytes_added_absolute",
        "bytes_added_pos",
        "bytes_added_neg",
        "edit_count"
      ],
      "type": "raw",
      "data": {
        "15972203": [
          683,
          1133,
          908,
          -225,
          5
        ],
        "13234584": [
          0,
          0,
          0,
          0,
          0
        ],
        "15972135": [
          0,
          0,
          0,
          0,
          0
        ]
      },
      "interval_hours": 24,
      "t": 24
    }

To save the contents to a file [-s] and timestamp the file [-t]:

    RFaulkner-WMF:umapi_client rfaulkner$ ./scripts/call_client "cohorts/\
    ryan_test_2/bytes_added" -s -t
    Mar-29 12:47:33 DEBUG    __main__ :: Attempting to create cookie jar,
        logging in ..
    Mar-29 12:47:34 DEBUG    __main__ :: Login successful. Making request:
        http://metrics.wikimedia.org/cohorts/ryan_test_2/bytes_added
    Mar-29 12:47:35 DEBUG    __main__ :: Writing response to file:
        umapi_client_ryan_test_2_bytes_added_20130329.json
    RFaulkner-WMF:umapi_client rfaulkner$ cat umapi_client_ryan_test_2_bytes_\
       added_20130329.json
    {
      "cohort": "ryan_test_2",
      "group": "default",
      "cohort_last_generated": "2013-03-29 19:40:19",
      "aggregator": "None",
      "metric": "bytes_added",
      "namespace": [
        0
      ],
      "project": "enwiki",
      "time_of_response": "2013-03-29 19:40:26",
      "datetime_start": "2010-10-25 08:00:00",
      "datetime_end": "2011-01-01 00:00:00",
      "header": [
        "user_id",
        "bytes_added_net",
        "bytes_added_absolute",
        "bytes_added_pos",
        "bytes_added_neg",
        "edit_count"
      ],
      "type": "raw",
      "data": {
        "15972203": [
          683,
          1133,
          908,
          -225,
          5
        ],
        "13234584": [
          0,
          0,
          0,
          0,
          0
        ],
        "15972135": [
          0,
          0,
          0,
          0,
          0
        ]
      },
      "interval_hours": 24,
      "t": 24
    }

To convert the output to csv:

    RFaulkner-WMF:scripts rfaulkner$ ./json2csv umapi_client_ryan_test_2_bytes_added_20130331.json
    Mar-31 23:57:20 DEBUG    __main__ :: Attempting to read file...
    Mar-31 23:57:20 DEBUG    __main__ :: Writing to file...
    RFaulkner-WMF:scripts rfaulkner$ cat ../../csv/umapi_client_ryan_test_2_bytes_added_20130331.json.csv
    user_id,bytes_added_net,bytes_added_absolute,bytes_added_pos,bytes_added_neg,edit_count
    13234584,0,0,0,0,0
    15972203,683,1133,908,-225,5
    15972135,0,0,0,0,0
