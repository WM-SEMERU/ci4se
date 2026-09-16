def assert_headers(context):
    expected_headers = [(k, v) for k, v in row_table(context).items()]
    request = httpretty.last_request()
    actual_headers = request.headers.items()
    for expected_header in expected_headers:
        assert_in(expected_header, actual_headers)