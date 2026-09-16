def stream_task_output(session, task_id, file_name, blocksize=
    DEFAULT_DOWNLOAD_BLOCK_SIZE):
    logger.debug('Streaming {} from task {}'.format(file_name, task_id))
    offset = 0
    contents = '[PLACEHOLDER]'
    while contents:
        contents = session.downloadTaskOutput(task_id, file_name, offset,
            blocksize)
        offset += len(contents)
        if contents:
            yield contents
    logger.debug('Finished streaming {} from task {}'.format(file_name,
        task_id))