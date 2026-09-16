def _extract_html_hex(string):
    try:
        hex_string = string and _hex_regexp().search(string).group(0) or ''
    except AttributeError:
        return None
    if len(hex_string) == 3:
        hex_string = hex_string[0] * 2 + hex_string[1] * 2 + hex_string[2] * 2
    return hex_string