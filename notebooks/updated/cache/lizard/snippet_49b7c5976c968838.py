def _find_name(self, name):
    name = name.upper()
    element = self.element.find_child_reference(name)
    return element['name'] if element is not None else None