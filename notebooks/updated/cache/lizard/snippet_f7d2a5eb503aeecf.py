def preservesurrogates(s):
    if not isinstance(s, six.text_type):
        raise TypeError("String to split must be of type 'unicode'!")
    surrogates_regex_str = '[{0}-{1}][{2}-{3}]'.format(HIGH_SURROGATE_START,
        HIGH_SURROGATE_END, LOW_SURROGATE_START, LOW_SURROGATE_END)
    surrogates_regex = re.compile('(?:{0})|.'.format(surrogates_regex_str))
    return surrogates_regex.findall(s)