def _xpathDict(xml, xpath, cls, parent, **kwargs):
    children = []
    for child in xml.xpath(xpath, namespaces=XPATH_NAMESPACES):
        children.append(cls.parse(resource=child, parent=parent, **kwargs))
    return children