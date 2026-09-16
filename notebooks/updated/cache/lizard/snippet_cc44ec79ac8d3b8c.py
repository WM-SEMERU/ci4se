def split_term_lower(cls, term):
    return tuple(e.lower() for e in Term.split_term(term))