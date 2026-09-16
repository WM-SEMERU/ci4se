def _inherit_context(self, node):
    xmlattrs = filter(_IN_XML_NS, _attrs(node))
    inherited, parent = [], node.parentNode
    while parent and parent.nodeType == Node.ELEMENT_NODE:
        for a in filter(_IN_XML_NS, _attrs(parent)):
            n = a.localName
            if n not in xmlattrs:
                xmlattrs.append(n)
                inherited.append(a)
        parent = parent.parentNode
    return inherited