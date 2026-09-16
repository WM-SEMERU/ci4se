def extract_headers(lines, max_wrap_lines):
    hdrs = {}
    header_name = None
    extend_lines = 0
    lines_processed = 0
    for n, line in enumerate(lines):
        if not line.strip():
            header_name = None
            continue
        match = HEADER_RE.match(line)
        if match:
            header_name, header_value = match.groups()
            header_name = header_name.strip().lower()
            extend_lines = 0
            if header_name in HEADER_MAP:
                hdrs[HEADER_MAP[header_name]] = header_value.strip()
            lines_processed = n + 1
        else:
            extend_lines += 1
            if extend_lines < max_wrap_lines and header_name in HEADER_MAP:
                hdrs[HEADER_MAP[header_name]] = join_wrapped_lines([hdrs[
                    HEADER_MAP[header_name]], line.strip()])
                lines_processed = n + 1
            else:
                break
    return hdrs, lines_processed