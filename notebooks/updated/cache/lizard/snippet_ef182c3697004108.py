def fixup_offsets(self, new_start, node):
    if hasattr(node, 'start'):
        node.start += new_start
        node.finish += new_start
    for n in node:
        if hasattr(n, 'offset'):
            if hasattr(n, 'start'):
                n.start += new_start
                n.finish += new_start
        else:
            self.fixup_offsets(new_start, n)
    return