def get_log_filehandle(context):
    log_file_name = get_log_filename(context)
    makedirs(context.config['task_log_dir'])
    with open(log_file_name, 'w', encoding='utf-8') as filehandle:
        yield filehandle