def set_renamed_input_fields(self, renamed_input_fields):
    if not (isinstance(renamed_input_fields, basestring) or isinstance(
        renamed_input_fields, ListType)):
        raise ValueError('renamed_input_fields must be a string or a list')
    self.renamed_input_fields = renamed_input_fields
    return self