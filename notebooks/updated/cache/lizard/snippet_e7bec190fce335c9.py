def _extract(node, name, index=0):
    nodes = node.getElementsByTagName(name)
    if len(nodes):
        if nodes[index].firstChild:
            return _unescape_htmlentity(nodes[index].firstChild.data.strip())
    else:
        return None