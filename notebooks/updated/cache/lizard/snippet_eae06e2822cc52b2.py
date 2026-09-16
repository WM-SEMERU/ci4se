def expand_include(filename):
    open_files = set()

    def _expand_include_rec(filename):
        if filename in open_files:
            raise RuntimeError(
                'Recursive include statement detected for file: ' + filename)
        else:
            open_files.add(filename)
        with open(filename) as open_file:
            for line in open_file:
                line_stripped = line.strip().replace('//', '#')
                if line_stripped.startswith('@include '):
                    inc_to_clean = line_stripped.split(None, 1)[1]
                    inc_filename = inc_to_clean.replace('"', ' ').strip()
                    for included_line in _expand_include_rec(inc_filename):
                        yield included_line
                else:
                    yield line
        open_files.remove(filename)
    try:
        lines = []
        for line in _expand_include_rec(filename):
            lines.append(line)
        return ''.join(lines)
    except RuntimeError:
        return None