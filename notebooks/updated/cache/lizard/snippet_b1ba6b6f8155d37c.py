def find_kw(ar_or_sample, kw):
    for analysis in find_analyses(ar_or_sample):
        if kw in get_interims_keywords(analysis):
            return analysis.getKeyword()
    return None