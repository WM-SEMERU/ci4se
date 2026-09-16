def load_file_template(path):
    template = StringIO()
    if not os.path.exists(path):
        raise ValueError('path does not exist: %s' % path)
    with open(clean_path(path), 'rb') as infile:
        for line in infile:
            template.write(line.decode('utf-8'))
    return template