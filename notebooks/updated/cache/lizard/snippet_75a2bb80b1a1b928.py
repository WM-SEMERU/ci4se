def get_property(self):
    variable_properties = {}
    for block in self.variable_block():
        name = self.name_expr.searchString(block)[0][0]
        properties = self.property_expr.searchString(block)
        variable_properties[name] = [y.strip() for x in properties for y in x]
    return variable_properties