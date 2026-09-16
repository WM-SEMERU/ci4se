def joinWords(text, separator=''):
    text = nativestring(text)
    output = separator.join(words(text.strip(separator)))
    if not separator:
        return output
    begin = re.match('^\\%s+' % separator, text)
    if begin:
        output = begin.group() + output
        if begin.group() == text:
            return output
    end = re.search('\\%s+$' % separator, text)
    if end:
        output += end.group()
    return output