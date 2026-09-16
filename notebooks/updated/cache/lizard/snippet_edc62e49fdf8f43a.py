def _term_query(self, term, field_name, field_type, stemmed=True):
    constructor = '{prefix}{term}'
    prefix = ''
    if field_name:
        prefix = TERM_PREFIXES['field'] + field_name.upper()
        term = _to_xapian_term(term)
    if field_name in (ID, DJANGO_ID, DJANGO_CT):
        if field_name == DJANGO_ID:
            term = int(term)
        term = _term_to_xapian_value(term, field_type)
        return xapian.Query('%s%s' % (TERM_PREFIXES[field_name], term))
    if field_type == 'datetime':
        date, time = term.split()
        return xapian.Query(xapian.Query.OP_AND_MAYBE, constructor.format(
            prefix=prefix, term=date), constructor.format(prefix=prefix,
            term=time))
    if field_type not in ('text', None):
        stemmed = False
    unstemmed_term = constructor.format(prefix=prefix, term=term)
    if stemmed:
        stem = xapian.Stem(self.backend.language)
        stemmed_term = 'Z' + constructor.format(prefix=prefix, term=stem(
            term).decode('utf-8'))
        return xapian.Query(xapian.Query.OP_OR, xapian.Query(stemmed_term),
            xapian.Query(unstemmed_term))
    else:
        return xapian.Query(unstemmed_term)