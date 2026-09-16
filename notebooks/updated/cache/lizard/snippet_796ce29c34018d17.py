def remove_external_references_from_roles(self):
    for node_role in self.node.findall('role'):
        role = Crole(node_role)
        role.remove_external_references()