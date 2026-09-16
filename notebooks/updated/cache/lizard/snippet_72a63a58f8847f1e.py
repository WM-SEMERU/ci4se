def innertext(node):
    if not len(node):
        return node.text
    return (node.text or '') + ''.join([etree.tostring(c) for c in node]) + (
        node.tail or '')