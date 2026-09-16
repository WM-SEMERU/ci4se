def get_task_output_description(task_output):
    output_description = 'n/a'
    if isinstance(task_output, RemoteTarget):
        output_description = '[SSH] {0}:{1}'.format(task_output._fs.
            remote_context.host, task_output.path)
    elif isinstance(task_output, S3Target):
        output_description = '[S3] {0}'.format(task_output.path)
    elif isinstance(task_output, FileSystemTarget):
        output_description = '[FileSystem] {0}'.format(task_output.path)
    elif isinstance(task_output, PostgresTarget):
        output_description = '[DB] {0}:{1}'.format(task_output.host,
            task_output.table)
    else:
        output_description = 'to be determined'
    return output_description