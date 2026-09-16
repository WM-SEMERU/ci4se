def relation(self, node):
    return self.query(select_block=str(node.attributes), from_block=node.name)