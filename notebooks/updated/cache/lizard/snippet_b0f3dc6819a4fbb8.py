def sources_to_nr_vars(sources):
    sources = default_sources(**sources)
    try:
        return OrderedDict((SOURCE_VAR_TYPES[name], nr) for name, nr in
            sources.iteritems())
    except KeyError as e:
        raise KeyError(
            'No source type %s is registered. Valid source types are %s' %
            (e, SOURCE_VAR_TYPES.keys()))