def _add_example(self, example):
    if len(example.fields) != 1:
        raise InvalidSpec('Example for union must specify exactly one tag.',
            example.lineno, example.path)
    example_field = list(example.fields.values())[0]
    tag = example_field.name
    for field in self.all_fields:
        if tag == field.name:
            break
    else:
        raise InvalidSpec("Unknown tag '%s' in example." % tag, example.
            lineno, example.path)
    try:
        field.data_type.check_example(example_field)
    except InvalidSpec as e:
        e.msg = "Bad example for field '{}': {}".format(field.name, e.msg)
        raise
    self._raw_examples[example.label] = example