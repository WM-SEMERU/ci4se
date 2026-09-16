def _resolve_available(self, tokens, context):
    from .gen.ExcellentParser import ExcellentParser
    has_missing = False
    output_components = []
    for t in range(len(tokens.tokens) - 1):
        token = tokens.get(t)
        next_token = tokens.get(t + 1)
        if (token.type == ExcellentParser.NAME and next_token.type !=
            ExcellentParser.LPAREN):
            try:
                output_components.append(context.resolve_variable(token.text))
            except EvaluationError:
                has_missing = True
                output_components.append(token)
        else:
            output_components.append(token)
    if not has_missing:
        return None
    output = [self._expression_prefix]
    for output_component in output_components:
        if isinstance(output_component, Token):
            comp_val = output_component.text
        else:
            comp_val = conversions.to_repr(output_component, context)
        output.append(comp_val)
    return ''.join(output)