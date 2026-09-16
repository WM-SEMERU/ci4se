def get_variables(self):
    variables = self.model.nodes()
    variable_tag = {}
    for var in sorted(variables):
        variable_tag[var] = etree.SubElement(self.network, 'VARIABLE',
            attrib={'TYPE': 'nature'})
        etree.SubElement(variable_tag[var], 'NAME').text = var
    return variable_tag