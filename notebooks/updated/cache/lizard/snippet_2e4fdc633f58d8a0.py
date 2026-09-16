def algorithm_to_text(value):
    text = _algorithm_by_value.get(value)
    if text is None:
        text = str(value)
    return text