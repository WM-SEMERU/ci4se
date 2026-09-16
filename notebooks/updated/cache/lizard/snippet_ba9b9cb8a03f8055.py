def set_output_fields(self, output_fields):
    if isinstance(output_fields, dict) or isinstance(output_fields, list):
        self.output_fields = output_fields
    elif isinstance(output_fields, basestring):
        self.output_field = output_fields
    else:
        raise ValueError('set_output_fields requires a dictionary of ' +
            'output fields to remap, a list of keys to filter, or a scalar string'
            )
    return self