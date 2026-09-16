def _get_recurse_directive_depth(field_name, field_directives):
    recurse_directive = field_directives['recurse']
    optional_directive = field_directives.get('optional', None)
    if optional_directive:
        raise GraphQLCompilationError(
            'Found both @optional and @recurse on the same vertex field: {}'
            .format(field_name))
    recurse_args = get_uniquely_named_objects_by_name(recurse_directive.
        arguments)
    recurse_depth = int(recurse_args['depth'].value.value)
    if recurse_depth < 1:
        raise GraphQLCompilationError(
            'Found recurse directive with disallowed depth: {}'.format(
            recurse_depth))
    return recurse_depth