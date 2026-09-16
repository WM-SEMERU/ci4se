def get_queue_obj(session, queue_url, log_url):
    skip = False
    if not queue_url:
        logger.error(
            'The queue url is not configured, skipping submit verification')
        skip = True
    if not session:
        logger.error('Missing requests session, skipping submit verification')
        skip = True
    queue = QueueSearch(session=session, queue_url=queue_url, log_url=log_url)
    queue.skip = skip
    return queue