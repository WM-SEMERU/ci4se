def get_lines_from_file(filename, lineno, context_lines, loader=None,
    module_name=None):
    lineno = lineno - 1
    lower_bound = max(0, lineno - context_lines)
    upper_bound = lineno + context_lines
    source = None
    if loader is not None and hasattr(loader, 'get_source'):
        result = get_source_lines_from_loader(loader, module_name, lineno,
            lower_bound, upper_bound)
        if result is not None:
            return result
    if source is None:
        try:
            with open(filename, 'rb') as file_obj:
                encoding = 'utf8'
                for line in itertools.islice(file_obj, 0, 2):
                    match = _coding_re.search(line.decode('utf8'))
                    if match:
                        encoding = match.group(1)
                        break
                file_obj.seek(0)
                lines = [compat.text_type(line, encoding, 'replace') for
                    line in itertools.islice(file_obj, lower_bound, 
                    upper_bound + 1)]
                offset = lineno - lower_bound
                return [l.strip('\r\n') for l in lines[0:offset]], lines[offset
                    ].strip('\r\n'), [l.strip('\r\n') for l in lines[offset +
                    1:]] if len(lines) > offset else []
        except (OSError, IOError, IndexError):
            pass
    return None, None, None