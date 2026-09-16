def parsecounts(table, field, parsers=(('int', int), ('float', float))):
    return ParseCountsView(table, field, parsers=parsers)