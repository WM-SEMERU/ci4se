def remove_tags(dirty, allowed_tags=(), allowed_trees=(), strip=None):
    if isinstance(dirty, six.string_types):
        element = etree.fromstring(''.join(('<DUMMYROOTTAG>', dirty,
            '</DUMMYROOTTAG>')))
    elif isinstance(dirty, etree._Element):
        element = dirty
    else:
        element = dirty.root
    if element.tag in allowed_trees:
        return etree.tostring(element, encoding='unicode')
    tail = element.tail or ''
    if strip and element.xpath(strip):
        return tail
    subtext = ''.join(remove_tags(child, allowed_tags=allowed_tags,
        allowed_trees=allowed_trees, strip=strip) for child in element)
    text = element.text or ''
    if element.tag in allowed_tags:
        for child in element:
            element.remove(child)
        element.text = ''.join((text, subtext))
        return etree.tostring(element, encoding='unicode')
    return ''.join((text, subtext, tail))