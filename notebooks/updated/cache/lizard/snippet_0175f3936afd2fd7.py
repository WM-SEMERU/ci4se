def _isrc_long(name=None):
    config = CWRTables()
    if name is None:
        name = 'ISRC Field'
    country = config.get_data('isrc_country_code')
    country_regex = ''
    for c in country:
        if len(country_regex) > 0:
            country_regex += '|'
        country_regex += c
    country_regex = '(' + country_regex + ')'
    field = pp.Regex(country_regex + '.{3}[0-9]{2}[0-9]{5}')
    field.setName(name)
    return field.setResultsName('isrc')