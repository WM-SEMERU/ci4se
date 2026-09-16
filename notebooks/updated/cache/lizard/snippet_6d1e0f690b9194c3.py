def from_string(cls, string, version):
    header, payload = string.split('\n', 1)
    if payload[0] == '\n':
        payload = payload[1:]
    if int(version) == 1:
        arc_header_re = ARC1_HEADER_RE
    elif int(version) == 2:
        arc_header_re = ARC2_HEADER_RE
    matches = arc_header_re.search(header)
    headers = matches.groupdict()
    arc_header = ARCHeader(**headers)
    return cls(header=arc_header, payload=payload, version=version)