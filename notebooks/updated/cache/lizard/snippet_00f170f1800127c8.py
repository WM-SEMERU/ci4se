def select(self, html, stype, expression):
    etree = html5lib.parse(html, treebuilder='lxml', namespaceHTMLElements=
        False)
    if stype == 'css':
        selector = lxml.cssselect.CSSSelector(expression)
        frag = list(selector(etree))
    else:
        frag = etree.xpath(expression)
    if not frag:
        raise RuntimeError('Nothing found for: %s' % expression)
    return ''.join([lxml.etree.tostring(x) for x in frag])