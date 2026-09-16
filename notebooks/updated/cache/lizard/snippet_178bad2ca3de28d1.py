def parse_pattern_list(liststr):
    _re_patt = re.compile('^(.*)=(.*)')
    patterns = []
    for ss in liststr.split(';'):
        match = _re_patt.match(ss)
        if match:
            desc = match.group(1)
            patt = match.group(2).split(',')
            patterns.append((desc, patt))
    return patterns