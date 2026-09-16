def load_re_from_file(filepath):
    regexp = None
    with open(filepath, 'r') as mlfile:
        flagstr = ''
        for line in mlfile:
            cleanline = re.sub('//.*$', '', line)
            if re.search('^\\s*$', cleanline):
                continue
            if re.search('^#.*$', cleanline):
                flagstr = cleanline[1:]
                continue
            if regexp is not None:
                raise Exception('Regular expression file format error')
            else:
                regexp = cleanline.rstrip('\n')
    flags = 0
    if 'i' in flagstr:
        flags |= re.I
    from pydsl.grammar.definition import RegularExpression
    return RegularExpression(regexp, flags)