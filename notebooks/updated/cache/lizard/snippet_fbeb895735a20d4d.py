def parse_path(self, node):
    if 'name' in node.lattrib:
        name = node.lattrib['name']
    else:
        self.raise_error('<Path> must specify a name.')
    description = node.lattrib.get('description', '')
    self.current_component_type.add_path(Path(name, description))