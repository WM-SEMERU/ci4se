def javascript_escape(s, quote_double_quotes=True):
    ustring_re = re.compile('([\x80-\uffff])')

    def fix(match):
        return '\\u%04x' % ord(match.group(1))
    if type(s) == str:
        s = s.decode('utf-8')
    elif type(s) != six.text_type:
        raise TypeError(s)
    s = s.replace('\\', '\\\\')
    s = s.replace('\r', '\\r')
    s = s.replace('\n', '\\n')
    s = s.replace('\t', '\\t')
    s = s.replace("'", "\\'")
    if quote_double_quotes:
        s = s.replace('"', '&quot;')
    return str(ustring_re.sub(fix, s))