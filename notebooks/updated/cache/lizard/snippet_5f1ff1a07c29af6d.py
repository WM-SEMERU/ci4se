def replace_variable(self, variable):
    if variable == 'x':
        return self.value
    if variable == 't':
        return self.timedelta
    raise ValueError('Invalid variable %s', variable)