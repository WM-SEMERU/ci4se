def removeNestedGroups(node):
    global _num_elements_removed
    num = 0
    groupsToRemove = []
    if not (node.nodeType == Node.ELEMENT_NODE and node.nodeName == 'switch'):
        for child in node.childNodes:
            if child.nodeName == 'g' and child.namespaceURI == NS['SVG'
                ] and len(child.attributes) == 0:
                for grandchild in child.childNodes:
                    if (grandchild.nodeType == Node.ELEMENT_NODE and 
                        grandchild.namespaceURI == NS['SVG'] and grandchild
                        .nodeName in ['title', 'desc']):
                        break
                else:
                    groupsToRemove.append(child)
    for g in groupsToRemove:
        while g.childNodes.length > 0:
            g.parentNode.insertBefore(g.firstChild, g)
        g.parentNode.removeChild(g)
        _num_elements_removed += 1
        num += 1
    for child in node.childNodes:
        if child.nodeType == Node.ELEMENT_NODE:
            num += removeNestedGroups(child)
    return num