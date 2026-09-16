def assert_equals(actual, expected, ignore_order=False, ignore_index=False,
    all_close=False):
    equals_, reason = equals(actual, expected, ignore_order, ignore_index,
        all_close, _return_reason=True)
    assert equals_, '{}\n\n{}\n\n{}'.format(reason, actual.to_string(),
        expected.to_string())