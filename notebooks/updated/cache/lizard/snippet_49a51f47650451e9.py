def _page_to_text(page):
    start_pos = page.find('<text')
    assert start_pos != -1
    end_tag_pos = page.find('>', start_pos)
    assert end_tag_pos != -1
    end_tag_pos += len('>')
    end_pos = page.find('</text>')
    if end_pos == -1:
        return ''
    return page[end_tag_pos:end_pos]