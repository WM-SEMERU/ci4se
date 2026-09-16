def _post_tidy(html):
    tree = etree.fromstring(html)
    ems = tree.xpath(
        "//xh:em[@class='underline']|//xh:em[contains(@class, ' underline ')]",
        namespaces={'xh': 'http://www.w3.org/1999/xhtml'})
    for el in ems:
        c = el.attrib.get('class', '').split()
        c.remove('underline')
        el.tag = '{http://www.w3.org/1999/xhtml}u'
        if c:
            el.attrib['class'] = ' '.join(c)
        elif 'class' in el.attrib:
            del el.attrib['class']
    return tree