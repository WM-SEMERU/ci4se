def debug(message, domain):
    if domain in Logger._ignored_domains:
        return
    Logger._log(None, message, DEBUG, domain)