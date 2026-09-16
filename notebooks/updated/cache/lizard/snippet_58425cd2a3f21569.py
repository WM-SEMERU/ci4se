def parse_derived_parameter(self, node):
    if 'name' in node.lattrib:
        name = node.lattrib['name']
    else:
        self.raise_error('A derived parameter must have a name')
    if 'dimension' in node.lattrib:
        dimension = node.lattrib['dimension']
    else:
        dimension = None
    if 'value' in node.lattrib:
        value = node.lattrib['value']
    else:
        value = None
    if 'select' in node.lattrib:
        select = node.lattrib['select']
    else:
        select = None
    self.current_component_type.add_derived_parameter(DerivedParameter(name,
        value, dimension, select))