def fromSearch(text):
    terms = []
    for term in nstr(text).split(','):
        if '*' not in term:
            term = '*%s*' % term
        term = term.replace('*', '.*')
        terms.append('^%s$' % term)
    return '|'.join(terms)