def add(self, child):
    if isinstance(child, Include):
        self.add_include(child)
    elif isinstance(child, Dimension):
        self.add_dimension(child)
    elif isinstance(child, Unit):
        self.add_unit(child)
    elif isinstance(child, ComponentType):
        self.add_component_type(child)
    elif isinstance(child, Component):
        self.add_component(child)
    elif isinstance(child, FatComponent):
        self.add_fat_component(child)
    elif isinstance(child, Constant):
        self.add_constant(child)
    else:
        raise ModelError('Unsupported child element')