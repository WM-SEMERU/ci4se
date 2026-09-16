def get_words(s, splitter_regex=rex.word_sep_except_external_appostrophe,
    preprocessor=strip_HTML, postprocessor=strip_edge_punc, min_len=None,
    max_len=None, blacklist=None, whitelist=None, lower=False, filter_fun=
    None, str_type=str):
    r
    postprocessor = postprocessor or str_type
    preprocessor = preprocessor or str_type
    if min_len is None:
        min_len = get_words.min_len
    if max_len is None:
        max_len = get_words.max_len
    blacklist = blacklist or get_words.blacklist
    whitelist = whitelist or get_words.whitelist
    filter_fun = filter_fun or get_words.filter_fun
    lower = lower or get_words.lower
    try:
        s = open(s, 'r')
    except (IOError, FileNotFoundError):
        pass
    try:
        s = s.read()
    except (IOError, AttributeError, TypeError):
        pass
    if not isinstance(s, basestring):
        try:
            return [word for obj in s for word in get_words(obj)]
        except (IOError, IndexError, ValueError, AttributeError, TypeError):
            pass
    try:
        s = preprocessor(s)
    except (IndexError, ValueError, AttributeError, TypeError):
        pass
    if isinstance(splitter_regex, basestring):
        splitter_regex = re.compile(splitter_regex)
    s = list(map(postprocessor, splitter_regex.split(s)))
    s = list(map(str_type, s))
    if not filter_fun:
        return s
    return [word for word in s if filter_fun(word, min_len=min_len, max_len
        =max_len, blacklist=blacklist, whitelist=whitelist, lower=lower)]