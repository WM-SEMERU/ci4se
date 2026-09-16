def _get_trail(request, exclude_section=False):
    trail = []
    url = request.path
    while url:
        if url == '/':
            break
        if exclude_section and url in SECTIONS:
            break
        crumb = find_crumb(request, url)
        if not crumb:
            break
        trail.append(crumb)
        url = urljoin(url, '..')
    trail.reverse()
    return trail