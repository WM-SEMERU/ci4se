def type_converter(text):
    if text.isdigit():
        return int(text), int
    try:
        return float(text), float
    except ValueError:
        return text, STRING_TYPE