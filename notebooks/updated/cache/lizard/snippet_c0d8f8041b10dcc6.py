def get_ii_text(node):
    if node.tag != 'IndicatorItem':
        raise IOCParseError('Invalid tag: {}'.format(node.tag))
    condition = node.attrib.get('condition')
    preserve_case = node.attrib.get('preserve-case', '')
    negate = node.attrib.get('negate', '')
    content = node.findtext('Content')
    search = node.find('Context').get('search')
    if preserve_case.lower() == 'true':
        preserve_case = ' (Preserve Case)'
    else:
        preserve_case = ''
    if negate.lower() == 'true':
        negate = 'NOT '
    else:
        negate = ''
    s = '{negate}{search} {condition} "{content}"{preserve_case}'.format(negate
        =negate, search=search, condition=condition, content=content,
        preserve_case=preserve_case)
    return s