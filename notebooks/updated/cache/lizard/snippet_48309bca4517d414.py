def _dump_to_pages(dump):
    pos = 0
    ret = []
    start_tag = '<page>\n'
    end_tag = '</page>\n'
    while True:
        start_pos = dump.find(start_tag, pos)
        if start_pos == -1:
            break
        start_pos += len(start_tag)
        end_pos = dump.find(end_tag, start_pos)
        if end_pos == -1:
            break
        ret.append(dump[start_pos:end_pos])
        pos = end_pos + len(end_tag)
    return ret