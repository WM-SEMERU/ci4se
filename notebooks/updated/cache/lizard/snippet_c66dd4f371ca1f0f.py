def set_parameter(self, key, value):
    for x in self.transformed_structures:
        x.other_parameters[key] = value