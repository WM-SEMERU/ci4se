def _filter_parameters(parameters):
    if not parameters:
        return None
    return OrderedDict((param, value) for param, value in six.iteritems(
        parameters) if param not in IGNORED_PARAMS)