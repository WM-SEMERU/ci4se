def get_file_name(query):
    match = re.search('\\S*\\.[\\d\\w]{1,4}', query)
    if match:
        filename = match.group()
        return filename
    else:
        start = match.start()
        end = match.end()
        spaces = re.finditer(' ', query)
        space_index = []
        for space in spaces:
            space_index.append(space.start())
        space_index.pop()
        for i in space_index:
            filename = query[i + 1:end]
            if os.path.isfile(filename):
                return filename
        return None