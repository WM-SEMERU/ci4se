def parse_time_derivative(self, node):
    if 'variable' in node.lattrib:
        variable = node.lattrib['variable']
    else:
        self.raise_error('<TimeDerivative> must specify a variable.')
    if 'value' in node.lattrib:
        value = node.lattrib['value']
    else:
        self.raise_error(
            "Time derivative for '{0}' must specify an expression.", variable)
    self.current_regime.add_time_derivative(TimeDerivative(variable, value))