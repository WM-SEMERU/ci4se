def assign_fields(self):
    queue = [(self.fields, {})]
    while queue:
        node, field_values = queue.pop(0)
        self._assign_fields(node.fields, field_values, assign_positions=False)
        for requirements, child in iteritems(node.children):
            requirements = dict(requirements)
            requirements.update(field_values)
            queue.append((child, requirements))

    def recurse_assign_fields(node=self.fields, field_values={}):
        for requirements, child in iteritems(node.children):
            child_field_values = dict(requirements)
            child_field_values.update(field_values)
            recurse_assign_fields(child, child_field_values)
        self._assign_fields(node.fields, field_values, assign_positions=True)
    recurse_assign_fields()