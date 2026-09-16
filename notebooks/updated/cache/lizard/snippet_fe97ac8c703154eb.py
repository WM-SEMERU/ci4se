def _clean_html(html):
    content = html.replace('&#x000A;', '\n').replace('¶', '')
    content = _LINK_PATTERN.sub('', content)
    content = _HTML_TAG_PATTERN.sub('', content)
    content = _BACKSLASH_PATTERN.sub('\n', content)
    return content