def assert_is_substring(substring, subject, message=None, extra=None):
    assert subject is not None and substring is not None and subject.find(
        substring) != -1, _assert_fail_message(message, substring, subject,
        'is not in', extra)