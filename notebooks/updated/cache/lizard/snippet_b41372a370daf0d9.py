def _get_parts_of_format_string(resolved_string, literal_texts, format_specs):
    _text = resolved_string
    bits = []
    if literal_texts[-1] != '' and _text.endswith(literal_texts[-1]):
        _text = _text[:-len(literal_texts[-1])]
        literal_texts = literal_texts[:-1]
        format_specs = format_specs[:-1]
    for i, literal_text in enumerate(literal_texts):
        if literal_text != '':
            if literal_text not in _text:
                raise ValueError(
                    "Resolved string must match pattern. '{}' not found.".
                    format(literal_text))
            bit, _text = _text.split(literal_text, 1)
            if bit:
                bits.append(bit)
        elif i == 0:
            continue
        else:
            try:
                format_spec = _validate_format_spec(format_specs[i - 1])
                bits.append(_text[0:format_spec])
                _text = _text[format_spec:]
            except:
                if i == len(format_specs) - 1:
                    format_spec = _validate_format_spec(format_specs[i])
                    bits.append(_text[:-format_spec])
                    bits.append(_text[-format_spec:])
                    _text = []
                else:
                    _validate_format_spec(format_specs[i - 1])
    if _text:
        bits.append(_text)
    if len(bits) > len([fs for fs in format_specs if fs is not None]):
        bits = bits[1:]
    return bits