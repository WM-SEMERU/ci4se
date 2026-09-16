def replace_urls(status):
    text = status.text
    if not has_url(status):
        return text
    urls = [(e['indices'], e['expanded_url']) for e in status.entities['urls']]
    urls.sort(key=lambda x: x[0][0], reverse=True)
    for (start, end), url in urls:
        text = text[:start] + url + text[end:]
    return text