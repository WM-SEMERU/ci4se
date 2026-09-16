def get_doc(additional_doc=False, field_prefix='$', field_suffix=':', indent=4
    ):
    if additional_doc:
        f = fields.copy()
        f.update(additional_doc)
    else:
        f = fields
    field_length = get_max_field_length(f)
    field_length = field_length + len(field_prefix) + len(field_suffix) + 4
    description_indent = ' ' * (indent + field_length)
    output = ''
    for field, description in sorted(f.items()):
        description = description['description']
        field = ' ' * indent + field_prefix + field + ':'
        output += field.ljust(field_length) + textwrap.fill(description,
            width=78, initial_indent=description_indent, subsequent_indent=
            description_indent)[field_length:] + '\n\n\n'
    return output