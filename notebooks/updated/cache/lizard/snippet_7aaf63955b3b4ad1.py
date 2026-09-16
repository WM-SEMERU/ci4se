def cookie_to_state(cookie_str, name, encryption_key):
    try:
        cookie = SimpleCookie(cookie_str)
        state = State(cookie[name].value, encryption_key)
    except KeyError as e:
        msg_tmpl = 'No cookie named {name} in {data}'
        msg = msg_tmpl.format(name=name, data=cookie_str)
        logger.exception(msg)
        raise SATOSAStateError(msg) from e
    except ValueError as e:
        msg_tmpl = 'Failed to process {name} from {data}'
        msg = msg_tmpl.format(name=name, data=cookie_str)
        logger.exception(msg)
        raise SATOSAStateError(msg) from e
    else:
        msg_tmpl = 'Loading state from cookie {data}'
        msg = msg_tmpl.format(data=cookie_str)
        satosa_logging(logger, logging.DEBUG, msg, state)
        return state