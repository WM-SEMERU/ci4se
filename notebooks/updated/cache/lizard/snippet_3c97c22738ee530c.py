def _parse_from_table(html_chunk, what):
    ean_tag = html_chunk.find('tr', fn=must_contain('th', what, 'td'))
    if not ean_tag:
        return None
    return get_first_content(ean_tag[0].find('td'))