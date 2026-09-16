def file_adapter(file_or_path):
    if is_file(file_or_path):
        file_obj = file_or_path
    else:
        file_obj = open(file_or_path, 'rb')
    yield file_obj
    file_obj.close()