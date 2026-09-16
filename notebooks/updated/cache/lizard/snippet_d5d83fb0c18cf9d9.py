def parse_etag_header(header):
    m = etag_header_re.match(header.strip())
    if not m:
        return []
    if m.group(1):
        return m.group(1)
    else:
        return etag_re.findall(header)