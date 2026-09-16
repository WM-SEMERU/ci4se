def _get_placeholders(sql_statement, parameters):
    placeholders = {}
    try:
        for match in REGEX_PATTERN_SQL_PLACEHOLDERS.findall(sql_statement):
            for i, placeholder_type in enumerate(PlaceholderType._values):
                placeholder_name = match[i]
                if placeholder_name:
                    placeholder_value = parameters[placeholder_name]
                    if placeholder_type == PlaceholderType.nested_list and (
                        isinstance(placeholder_value, tuple) and len(
                        placeholder_value) == 1) and not isinstance(
                        placeholder_value, (list, set, tuple)):
                        raise ValueError(
                            'The value to replace the placeholder "%s" is not a list as expected'
                             % placeholder_name)
                    placeholders[placeholder_name
                        ] = placeholder_type, placeholder_value
                    break
    except KeyError:
        raise ValueError(
            'The placeholder %s has no corresponding parameter' %
            placeholder_name)
    undefined_placeholders = [parameter for parameter in parameters.
        iterkeys() if parameter not in placeholders]
    if undefined_placeholders:
        raise ValueError(
            """The placeholders %s are missing from the extended pyformat SQL statement
%s"""
             % (', '.join([('"%s"' % _) for _ in undefined_placeholders]),
            sql_statement))
    return placeholders