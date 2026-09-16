def removeDefaultAttributeValue(node, attribute):
    if not node.hasAttribute(attribute.name):
        return 0
    if isinstance(attribute.value, str):
        if node.getAttribute(attribute.name) == attribute.value:
            if attribute.conditions is None or attribute.conditions(node):
                node.removeAttribute(attribute.name)
                return 1
    else:
        nodeValue = SVGLength(node.getAttribute(attribute.name))
        if (attribute.value is None or nodeValue.value == attribute.value and
            not nodeValue.units == Unit.INVALID):
            if (attribute.units is None or nodeValue.units == attribute.
                units or isinstance(attribute.units, list) and nodeValue.
                units in attribute.units):
                if attribute.conditions is None or attribute.conditions(node):
                    node.removeAttribute(attribute.name)
                    return 1
    return 0