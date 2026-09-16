def get_column_names_from_file(file_path):
    if file_path.endswith('.gz'):
        file_handler = io.TextIOWrapper(io.BufferedReader(gzip.open(file_path))
            )
    else:
        file_handler = open(file_path, 'r')
    fields_line = False
    with file_handler as file:
        for line in file:
            line = line.strip()
            if not fields_line and re.search('#\\s*Fields\\s*:$', line):
                fields_line = True
            elif fields_line and not (line == '' or line == '#'):
                return [column.strip() for column in line[1:].split('\t')]