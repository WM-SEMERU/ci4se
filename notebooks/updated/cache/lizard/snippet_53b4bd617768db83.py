def international_str(self, name, sdmxobj):
    elem_attrib = self._paths['int_str_names'](sdmxobj._elem, name=name)
    values = self._paths['int_str_values'](sdmxobj._elem, name=name)
    if not elem_attrib:
        elem_attrib = ['en']
    return DictLike(zip(elem_attrib, values))