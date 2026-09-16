def is_email(data):
    if re.match('[\\w.%+-]+@[\\w.]+\\.[a-zA-Z]{2,4}', data):
        LOGGER.debug("> {0}' is matched as email.".format(data))
        return True
    else:
        LOGGER.debug("> {0}' is not matched as email.".format(data))
        return False