def field(self, name, fieldType='C', size='50', decimal=0):
    self.fields.append((name, fieldType, size, decimal))