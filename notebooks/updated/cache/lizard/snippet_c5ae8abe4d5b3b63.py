def criteria_text(self, sep='  ', params=False):
    s = ''
    criteria_node = self.root.find('criteria')
    if criteria_node is None:
        return s
    node_texts = []
    for node in criteria_node.getchildren():
        nt = self.get_node_text(node, depth=0, sep=sep, params=params)
        node_texts.append(nt)
    s = '\n'.join(node_texts)
    return s