def get_parsed_context(context_arg):
    if not context_arg:
        logger.debug(
            'pipeline invoked without context arg set. For this json parser you\'re looking for something like: pypyr pipelinename \'{"key1":"value1","key2":"value2"}\''
            )
        return None
    logger.debug('starting')
    return json.loads(context_arg)