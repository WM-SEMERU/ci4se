def _find_exclude_filter(cls, excludes, item):
    if excludes is None:
        return False

    def test_each_exclude(exclude_value):

        def exclude_equals_value_test(exclude_filter):
            if callable(exclude_filter):
                return exclude_filter(cls, item, exclude_value)
            return item.get(exclude_filter) == exclude_value
        return any(map(exclude_equals_value_test, cls.EXCLUDE_FILTERS))
    return any(map(test_each_exclude, excludes))