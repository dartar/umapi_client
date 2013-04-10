umapi_client
============

Client wrapper for Wikipedia User Metrics API.

See https://github.com/wikimedia/user_metrics for UMAPI implementation.

Getting UMAPI Responses with call_client
----------------------------------------

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


Converting Output to CSV
------------------------

To convert the output to csv:

    RFaulkner-WMF:scripts rfaulkner$ ./json2csv umapi_client_ryan_test_2_bytes_added_20130331.json
    Mar-31 23:57:20 DEBUG    __main__ :: Attempting to read file...
    Mar-31 23:57:20 DEBUG    __main__ :: Writing to file...
    RFaulkner-WMF:scripts rfaulkner$ cat ../../csv/umapi_client_ryan_test_2_bytes_added_20130331.json.csv
    user_id,bytes_added_net,bytes_added_absolute,bytes_added_pos,bytes_added_neg,edit_count
    13234584,0,0,0,0,0
    15972203,683,1133,908,-225,5
    15972135,0,0,0,0,0

Now, it is more convenient to be able to setup a list of jobs to run.  You could create a csv that looks
something like the following:

    cohorts/107~108~109~110~114~115~117/bytes_added?start=20120201&end=20120301&group=input&project=arwiki,
    cohorts/107~108~109~110~114~115~117/bytes_added?start=20120301&end=20120401&group=input&project=arwiki,
    cohorts/107~108~109~110~114~115~117/bytes_added?start=20120401&end=20120501&group=input&project=arwiki,
    ...

If you now call call_client with the -f flag followed by the in file name (the input file must exist in
<PROJECT_HOME>/input/) and then call json2csv over the resulting output you get the

    RFaulkner-WMF:scripts rfaulkner$ ./call_client -f in.txt -s -t
    RFaulkner-WMF:scripts rfaulkner$ ./json2csv ../../json/*
    RFaulkner-WMF:scripts rfaulkner$ head -n 10 ../../csv/umapi_client_107~108~109~110~114~115~117_bytes_addedQ\
        start-20120501_end-20120601_group-input_project-arwiki_20130407.json.csv

    user_id,bytes_added_net,bytes_added_absolute,bytes_added_pos,bytes_added_neg,edit_count
    469199,-4231,67235,31502,-35733,121
    471261,9484,9484,9484,0,1
    467685,0,0,0,0,0
    469196,0,0,0,0,0
    477445,54919,55561,55240,-321,42
    469224,0,0,0,0,0
    469189,0,0,0,0,0
    477440,4,4,4,0,1
    466000,18762,18872,18817,-55,6


User ID to Username Conversion
------------------------------

Here the script ``uid2username`` can be very helpful:

    RFaulkner-WMF:scripts rfaulkner$ ./uid2username -u 13234584 -o
    Apr-09 17:54:11 DEBUG    __main__ :: Setting up.
    Apr-09 17:54:12 DEBUG    __main__ :: Processing: 13234584.
    {"13234584": "Renklauf"}
    Apr-09 17:54:12 DEBUG    __main__ :: Shutting down.

The -u flag specifies the user ID to read, -o specifies print to stdout.  Similar to ``json2csv`` -f can
be used to specify a comma separated value file of user names and -s can be used to save the json output.