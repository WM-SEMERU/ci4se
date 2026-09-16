def format_explanation(explanation, original_msg=None):
    if not conf.is_message_introspection_enabled() and original_msg:
        return original_msg
    explanation = ecu(explanation)
    lines = _split_explanation(explanation)
    result = _format_lines(lines)
    return u('\n').join(result)