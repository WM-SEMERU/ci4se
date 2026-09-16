def stdout_notifications(notifications):
    for error in notifications['errors']:
        LOGGER.error(error)
    for warn in notifications['warnings']:
        LOGGER.warning(warn)