def _parse_parameter(tag, parser, parent):
    name, modifiers, dtype, kind = _parse_common(tag)
    if 'default' in tag.attrib:
        default = tag.attrib['default']
    else:
        default = None
    if 'dimension' in tag.attrib:
        dimension = tag.attrib['dimension']
    else:
        dimension = None
    result = ValueElement(name, modifiers, dtype, kind, default, dimension,
        parent)
    doc = DocElement(tag, parser, result)
    result.docstring.append(doc)
    parent.add_parameter(result)