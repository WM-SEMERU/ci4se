def get_text(revision, strip=True):
    start_pos = revision.find('<text')
    assert start_pos != -1
    end_tag_pos = revision.find('>', start_pos)
    assert end_tag_pos != -1
    end_tag_pos += len('>')
    end_pos = revision.find('</text>')
    if end_pos == -1:
        ret = ''
    else:
        ret = revision[end_tag_pos:end_pos]
    if strip:
        ret = strip_text(ret)
    ret = text_encoder.to_unicode_utf8(ret)
    return ret