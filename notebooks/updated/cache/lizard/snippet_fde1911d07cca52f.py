def templates(self):
    templates = {}
    result = []
    if self.entry_point_group_templates:
        result = self.load_entry_point_group_templates(self.
            entry_point_group_templates) or []
    for template in result:
        for name, path in template.items():
            templates[name] = path
    return templates