def output(file_like_object, path, verbose=False):
    if not path:
        for line in file_like_object:
            if verbose:
                print_info(line.rstrip())
            else:
                print(line.rstrip())
    else:
        try:
            object_file = open(os.path.expanduser(path), 'w', encoding='utf-8')
            shutil.copyfileobj(file_like_object, object_file)
            object_file.close()
        except EnvironmentError as xxx_todo_changeme:
            errno, strerror = xxx_todo_changeme.args
            error_line_list = ['Could not write to object_file: {}'.format(
                path), 'I/O error({}): {}'.format(errno, strerror)]
            error_message = '\n'.join(error_line_list)
            raise d1_cli.impl.exceptions.CLIError(error_message)