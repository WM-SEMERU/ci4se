def parse_drawing(document, container, elem):
    _blip = elem.xpath('.//a:blip', namespaces=NAMESPACES)
    if len(_blip) > 0:
        blip = _blip[0]
        _rid = blip.attrib[_name('{{{r}}}embed')]
        img = doc.Image(_rid)
        container.elements.append(img)