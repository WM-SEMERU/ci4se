def add_property(self, pid, label, term_span):
    node_prop = self.node.find('properties')
    if node_prop is None:
        properties = Cproperties(type=self.type)
        self.node.append(properties.get_node())
    else:
        properties = Cproperties(node=node_prop, type=self.type)
    properties.add_property(pid, label, term_span)