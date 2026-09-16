def extract_pdbid(string):
    p = re.compile('[0-9][0-9a-z]{3}')
    m = p.search(string.lower())
    try:
        return m.group()
    except AttributeError:
        return 'UnknownProtein'