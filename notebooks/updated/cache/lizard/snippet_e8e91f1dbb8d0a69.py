def parameterize(string, separator='-'):
    string = transliterate(string)
    string = re.sub('(?i)[^a-z0-9\\-_]+', separator, string)
    if separator:
        re_sep = re.escape(separator)
        string = re.sub('%s{2,}' % re_sep, separator, string)
        string = re.sub('(?i)^%(sep)s|%(sep)s$' % {'sep': re_sep}, '', string)
    return string.lower()