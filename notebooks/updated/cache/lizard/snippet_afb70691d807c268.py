def remove_properties(self):
    node_prop = self.node.find('properties')
    if node_prop is not None:
        self.node.remove(node_prop)