def convert_html_entities(text_string):
    if text_string is None or text_string == '':
        return ''
    elif isinstance(text_string, str):
        return html.unescape(text_string).replace('&quot;', "'")
    else:
        raise InputError('string not passed as argument for text_string')