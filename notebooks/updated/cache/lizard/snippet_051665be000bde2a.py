def extract_author_keywords(skw_db, ckw_db, fulltext):
    akw = {}
    for k, v in get_author_keywords(skw_db, ckw_db, fulltext).items():
        akw[KeywordToken(k, type='author-kw')] = v
    return akw