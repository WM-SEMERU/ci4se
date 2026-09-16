def get_process_definition_start(fname, slug):
    with open(fname) as file_:
        for i, line in enumerate(file_):
            if re.search('slug:\\s*{}'.format(slug), line):
                return i + 1
    return 1