def _get_acronyms(acronyms):
    acronyms_str = {}
    if acronyms:
        for acronym, expansions in iteritems(acronyms):
            expansions_str = ', '.join([('%s (%d)' % expansion) for
                expansion in expansions])
            acronyms_str[acronym] = expansions_str
    return [{'acronym': str(key), 'expansion': value.encode('utf8')} for 
        key, value in acronyms_str.iteritems()]