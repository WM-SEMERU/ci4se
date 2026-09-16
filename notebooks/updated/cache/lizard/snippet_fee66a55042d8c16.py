def _shorten_file_path(line):
    start = line.lower().find('file')
    if start < 0:
        return line
    first_quote = line.find('"', start)
    if first_quote < 0:
        return line
    second_quote = line.find('"', first_quote + 1)
    if second_quote < 0:
        return line
    path = line[first_quote + 1:second_quote]
    new_path = '/'.join(path.split('/')[-3:])
    return line[:first_quote] + '[...]/' + new_path + line[second_quote + 1:]