def write_file(path, data, format=True):
    if format:
        fs.write_file(path, format_json(data))
    else:
        fs.write_file(path, json.dumps(data))