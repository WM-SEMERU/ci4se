def add_node(self, variable):
    variable_name = variable.attrib['name']
    self.probnet['Variables'][variable_name] = {}
    self.probnet['Variables'][variable_name]['type'] = variable.attrib['type']
    self.probnet['Variables'][variable_name]['role'] = variable.attrib['role']
    if variable.find('Comment') is not None:
        self.probnet['Variables'][variable_name]['Comment'] = variable.find(
            'Comment').text
    if variable.find('Coordinates') is not None:
        self.probnet['Variables'][variable_name]['Coordinates'
            ] = variable.find('Coordinates').attrib
    if variable.find('AdditionalProperties/Property') is not None:
        self.probnet['Variables'][variable_name]['AdditionalProperties'] = {}
        for prop in variable.findall('AdditionalProperties/Property'):
            self.probnet['Variables'][variable_name]['AdditionalProperties'][
                prop.attrib['name']] = prop.attrib['value']
    if variable.find('States/State') is None:
        warnings.warn('States not available for node: ' + variable_name)
    else:
        self.probnet['Variables'][variable_name]['States'] = {state.attrib[
            'name']: {prop.attrib['name']: prop.attrib['value'] for prop in
            state.findall('AdditionalProperties/Property')} for state in
            variable.findall('States/State')}