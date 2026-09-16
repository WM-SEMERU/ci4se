def sanitize(url, config):
    if url.scheme not in ('postgres', 'postgresql', 'postgis'):
        raise ValueError("Unsupported database type: '%s'" % (url.scheme,))
    process = subprocess.Popen(('pg_dump', '--encoding=utf-8',
        '--quote-all-identifiers', '--dbname', url.geturl().replace(
        'postgis://', 'postgresql://')), stdout=subprocess.PIPE)
    sanitize_value_line = None
    current_table = None
    current_table_columns = None
    for line in io.TextIOWrapper(process.stdout, encoding='utf-8'):
        line = line.rstrip('\n')
        if current_table:
            if line == '\\.':
                current_table = None
                current_table_columns = None
                yield '\\.'
                continue
            if not sanitize_value_line:
                yield line
                continue
            yield sanitize_value_line(line)
            continue
        copy_line_match = COPY_LINE_PATTERN.match(line)
        if not copy_line_match:
            yield line
            continue
        current_table = copy_line_match.group('table')
        current_table_columns = parse_column_names(copy_line_match.group(
            'columns'))
        sanitize_value_line = get_value_line_sanitizer(config,
            current_table, current_table_columns)
        yield line