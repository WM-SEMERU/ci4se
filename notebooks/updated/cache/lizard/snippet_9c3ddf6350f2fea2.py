def uncomment(lines, prefix='#'):
    if not prefix:
        return lines
    prefix_and_space = prefix + ' '
    length_prefix = len(prefix)
    length_prefix_and_space = len(prefix_and_space)
    return [(line[length_prefix_and_space:] if line.startswith(
        prefix_and_space) else line[length_prefix:] if line.startswith(
        prefix) else line) for line in lines]