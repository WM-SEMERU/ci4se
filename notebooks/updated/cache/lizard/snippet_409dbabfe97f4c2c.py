def _compile_output_step(outputs):
    if not outputs:
        raise GraphQLCompilationError(
            'No fields were selected for output! Please mark at least one field with the @output directive.'
            )
    output_fields = {}
    for output_name, output_context in six.iteritems(outputs):
        location = output_context['location']
        optional = output_context['optional']
        graphql_type = output_context['type']
        expression = None
        existence_check = None
        if isinstance(location, FoldScopeLocation):
            if optional:
                raise AssertionError(
                    'Unreachable state reached, optional in fold: {}'.
                    format(output_context))
            if location.field == COUNT_META_FIELD_NAME:
                expression = expressions.FoldCountContextField(location)
            else:
                expression = expressions.FoldedContextField(location,
                    graphql_type)
        else:
            expression = expressions.OutputContextField(location, graphql_type)
            if optional:
                existence_check = expressions.ContextFieldExistence(location
                    .at_vertex())
        if existence_check:
            expression = expressions.TernaryConditional(existence_check,
                expression, expressions.NullLiteral)
        output_fields[output_name] = expression
    return blocks.ConstructResult(output_fields)