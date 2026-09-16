def assert_is(expected, actual, message=None, extra=None):
    assert expected is actual, _assert_fail_message(message, expected,
        actual, 'is not', extra)