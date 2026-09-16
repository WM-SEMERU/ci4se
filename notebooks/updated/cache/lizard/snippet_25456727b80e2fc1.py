def _uax44lm2transform(s):
    result = s
    medialhyphen = re.compile('(?<=\\w)-(?=\\w)')
    whitespaceunderscore = re.compile('[\\s_]', re.UNICODE)
    if result != 'HANGUL JUNGSEONG O-E':
        result = medialhyphen.sub('', result)
    result = whitespaceunderscore.sub('', result)
    return result.lower()