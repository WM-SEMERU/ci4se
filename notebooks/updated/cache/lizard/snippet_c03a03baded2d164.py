def split_comma_argument(comma_sep_str):
    terms = []
    for term in comma_sep_str.split(','):
        if term:
            terms.append(term)
    return terms