def strings_equal(s1, s2):
    try:
        s1 = unicodedata.normalize('NFKC', str(s1))
        s2 = unicodedata.normalize('NFKC', str(s2))
    except:
        s1 = unicodedata.normalize('NFKC', unicode(s1))
        s2 = unicodedata.normalize('NFKC', unicode(s2))
    return compare_digest(s1, s2)