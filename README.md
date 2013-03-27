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
be queued by the service. ::


    RFaulkner-WMF:umapi_client rfaulkner$ cd umapi_client/
    RFaulkner-WMF:umapi_client rfaulkner$ ./call_client cohorts/ryan_test_2/\
    bytes_added
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
