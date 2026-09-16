def propagate_occur(self, node, value):
    while node.occur < value:
        node.occur = value
        if node.name == 'define':
            break
        node = node.parent