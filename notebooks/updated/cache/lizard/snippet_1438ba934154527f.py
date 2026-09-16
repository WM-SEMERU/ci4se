def include_file_cb(include_path, line_ranges, symbol):
    lang = ''
    if include_path.endswith(('.md', '.markdown')):
        lang = 'markdown'
    else:
        split = os.path.splitext(include_path)
        if len(split) == 2:
            ext = split[1].strip('.')
            lang = LANG_MAPPING.get(ext) or ext
    if line_ranges:
        res = []
        for line_range in line_ranges:
            for lineno in range(line_range[0] + 1, line_range[1] + 1):
                line = linecache.getline(include_path, lineno)
                if not line:
                    return None
                res.append(line)
        return ''.join(res), lang
    with io.open(include_path, 'r', encoding='utf-8') as _:
        return _.read(), lang