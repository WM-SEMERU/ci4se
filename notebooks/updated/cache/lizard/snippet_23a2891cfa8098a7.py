def configure(**kwargs):
    for key in kwargs:
        if key == 'is_logging_enabled':
            Event.is_logging_enabled = kwargs[key]
        elif key == 'collector_queue':
            Event.collector_queue = kwargs[key]
        else:
            Logger.get_logger(__name__).error(
                'Unknown key %s in configure or bad type %s', key, type(
                kwargs[key]))