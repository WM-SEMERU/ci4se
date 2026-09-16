def validate_types(schemas_and_tables):
    all_types = get_types()
    if not all(sn in all_types for sn, tn in schemas_and_tables):
        bad_types = [sn for sn, tn in schemas_and_tables if sn not in all_types
            ]
        msg = '{} are invalid types'.format(bad_types)
        raise UnknownAnnotationTypeException(msg)