def fix_filename(path):
    r
    path_parts = path.split('/' if os.name == 'posix' else '\\')
    dir_parts = path_parts[:-1]
    filename = path_parts[-1]
    file_parts = filename.split('.')
    if len(file_parts) > 2:
        filename = '{' + '.'.join(file_parts[0:-1]) + '}.' + file_parts[-1]
    dir_parts.append(filename)
    fixed_path = '/'.join(dir_parts)
    if '~' in fixed_path:
        fixed_path = '\\detokenize{' + fixed_path + '}'
    return fixed_path