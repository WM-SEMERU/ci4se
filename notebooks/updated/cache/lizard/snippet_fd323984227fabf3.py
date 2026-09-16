def write_file(file_path, content):
    handler = open(file_path, 'w+')
    handler.write(content)
    handler.close()