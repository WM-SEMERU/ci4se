def sanitize_filename(filename):
    sanitized_filename = re.sub('[/\\\\:*?"<>|]', '-', filename)
    sanitized_filename = sanitized_filename.replace('&', 'and')
    sanitized_filename = sanitized_filename.replace('"', '')
    sanitized_filename = sanitized_filename.replace("'", '')
    sanitized_filename = sanitized_filename.replace('/', '')
    sanitized_filename = sanitized_filename.replace('\\', '')
    if sanitized_filename[0] == '.':
        sanitized_filename = 'dot' + sanitized_filename[1:]
    return sanitized_filename