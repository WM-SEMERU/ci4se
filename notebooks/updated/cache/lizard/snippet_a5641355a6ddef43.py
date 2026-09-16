def tag(tagname, content='', attrs=None):
    attrs_str = attrs and ' '.join(_generate_dom_attrs(attrs))
    open_tag = tagname
    if attrs_str:
        open_tag += ' ' + attrs_str
    if content is None:
        return literal('<%s />' % open_tag)
    content = ''.join(iterate(content, unless=(basestring, literal)))
    return literal('<%s>%s</%s>' % (open_tag, content, tagname))