def _assertion(self, matcher, value):
    if isinstance(value, Expectation):
        assertion = value._assertion.__get__(self, Expectation)
        assertion(matcher, value.value)
    else:
        hc.assert_that(value, matcher)