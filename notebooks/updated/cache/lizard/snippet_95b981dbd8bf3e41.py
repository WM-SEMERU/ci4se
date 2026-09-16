def active_path(context, pattern, css=None):
    request = context['request']
    if re.search(pattern, request.path):
        return css if css else 'active'
    return ''