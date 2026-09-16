def _ReduceParserFilters(cls, includes, excludes):
    if not includes or not excludes:
        return
    for parser_name in set(includes).intersection(excludes):
        if includes[parser_name] == excludes[parser_name]:
            logger.warning(
                'Parser {0:s} was in both the inclusion and exclusion lists. Ignoring included parser.'
                .format(parser_name))
            includes.pop(parser_name)
            continue
        plugin_includes = includes[parser_name]
        plugin_excludes = excludes[parser_name]
        intersection = set(plugin_includes).intersection(plugin_excludes)
        if not intersection:
            continue
        logger.warning(
            'Parser {0:s} plugins: {1:s} in both the inclusion and exclusion lists. Ignoring included plugins.'
            .format(parser_name, ', '.join(intersection)))
        plugins_list = list(set(plugin_includes).difference(intersection))
        includes[parser_name] = plugins_list
    parsers_to_pop = []
    for parser_name in excludes:
        if parser_name in includes:
            continue
        logger.warning(
            'The excluded parser: {0:s} is not associated with the included parsers: {1:s}. Ignoring excluded parser.'
            .format(parser_name, ', '.join(includes.keys())))
        parsers_to_pop.append(parser_name)
    for parser_name in parsers_to_pop:
        excludes.pop(parser_name)