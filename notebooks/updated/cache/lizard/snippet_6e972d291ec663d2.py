def get_version_naive(cls, name, ignore=''):
    match = cls._get_regex_search(name, cls.REGEX_VERSION.format(SEP=cls.
        REGEX_SEPARATORS), ignore=ignore)
    if match is not None:
        if len(match) > 1:
            for m in match:
                m.update({'version': int(m['match'].upper().replace('V', ''))})
            compound_version = '.'.join([str(m['version']) for m in match])
            compound_version = float(compound_version
                ) if compound_version.count('.') == 1 else compound_version
            return {'compound_matches': match, 'compound_version':
                compound_version, 'pattern': match[0]['pattern'], 'input':
                match[0]['input']}
        elif len(match) == 1:
            match = match[0]
            match.update({'version': int(match['match'].upper().replace('V',
                ''))})
            return match
    return None