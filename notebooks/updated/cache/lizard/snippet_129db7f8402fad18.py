def get_first_content(el_list, alt=None, strip=True):
    if not el_list:
        return alt
    content = el_list[0].getContent()
    if strip:
        content = content.strip()
    if not content:
        return alt
    return content