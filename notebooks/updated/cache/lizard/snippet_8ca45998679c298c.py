def _assert_type_bounds_are_not_conflicting(current_type_bound,
    previous_type_bound, location, match_query):
    if all((current_type_bound is not None, previous_type_bound is not None,
        current_type_bound != previous_type_bound)):
        raise AssertionError(
            'Conflicting type bounds calculated at location {}: {} vs {} for query {}'
            .format(location, previous_type_bound, current_type_bound,
            match_query))