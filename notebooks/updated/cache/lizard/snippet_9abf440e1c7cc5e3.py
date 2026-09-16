def _construct_location_stack_entry(location, num_traverses):
    if not isinstance(num_traverses, int) or num_traverses < 0:
        raise AssertionError(
            'Attempted to create a LocationStackEntry namedtuple with an invalid value for "num_traverses" {}. This is not allowed.'
            .format(num_traverses))
    if not isinstance(location, Location):
        raise AssertionError(
            'Attempted to create a LocationStackEntry namedtuple with an invalid value for "location" {}. This is not allowed.'
            .format(location))
    return LocationStackEntry(location=location, num_traverses=num_traverses)