def assert_in_with_tolerance(obj, seq, tolerance, message=None, extra=None):
    for i in seq:
        try:
            assert_eq(obj, i, tolerance=tolerance, message=message, extra=extra
                )
            return
        except AssertionError:
            pass
    assert False, _assert_fail_message(message, obj, seq, 'is not in', extra)