def _parse_content_type(self, value):
    content_type, params = parse_header(value)
    if 'charset' in params:
        charset = params['charset']
    else:
        charset = None
    return content_type, charset