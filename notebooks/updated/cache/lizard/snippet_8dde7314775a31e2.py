def find_python(finder, line=None):
    if line and not isinstance(line, six.string_types):
        raise TypeError(
            'Invalid python search type: expected string, received {0!r}'.
            format(line))
    if line and os.path.isabs(line):
        if os.name == 'nt':
            line = posixpath.join(*line.split(os.path.sep))
        return line
    if not finder:
        from pipenv.vendor.pythonfinder import Finder
        finder = Finder(global_search=True)
    if not line:
        result = next(iter(finder.find_all_python_versions()), None)
    elif line and line[0].isdigit() or re.match('[\\d\\.]+', line):
        result = finder.find_python_version(line)
    else:
        result = finder.find_python_version(name=line)
    if not result:
        result = finder.which(line)
    if not result and not line.startswith('python'):
        line = 'python{0}'.format(line)
        result = find_python(finder, line)
    if not result:
        result = next(iter(finder.find_all_python_versions()), None)
    if result:
        if not isinstance(result, six.string_types):
            return result.path.as_posix()
        return result
    return