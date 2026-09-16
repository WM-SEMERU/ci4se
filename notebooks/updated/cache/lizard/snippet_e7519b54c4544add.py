def _set_options_from_file(self, file_handle):
    options = []
    line_number = 0
    section = None
    for line in file_handle.read().splitlines():
        line_number += 1
        orig_line = line
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if line.startswith('[') and line.endswith(']'):
            section = line.strip('[]')
            continue
        if not section:
            raise ValueError(
                'Unable to parse unit file; Unexpected line outside of a section: {0} (line: {1}'
                .format(line, line_number))
        continuation = False
        try:
            if options[-1]['value'].endswith('\\'):
                options[-1]['value'] = options[-1]['value'][:-1]
                continuation = True
        except IndexError:
            pass
        try:
            if continuation:
                options[-1]['value'] += orig_line
                continue
            name, value = line.split('=', 1)
            options.append({'section': section, 'name': name, 'value': value})
        except ValueError:
            raise ValueError(
                'Unable to parse unit file; Malformed line in section {0}: {1} (line: {2})'
                .format(section, line, line_number))
    self._data['options'] = options
    return True