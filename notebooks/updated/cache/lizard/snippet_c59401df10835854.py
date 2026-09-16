def file_name_generator_recursive(path):
    for name in os.listdir(path):
        full_name = os.path.join(path, name)
        if os.path.isdir(full_name):
            for new_name in file_name_generator_recursive(full_name):
                yield new_name
        else:
            yield full_name