def before_sleep_log(logger, log_level):

    def log_it(retry_state):
        if retry_state.outcome.failed:
            verb, value = 'raised', retry_state.outcome.exception()
        else:
            verb, value = 'returned', retry_state.outcome.result()
        logger.log(log_level, 'Retrying %s in %s seconds as it %s %s.',
            _utils.get_callback_name(retry_state.fn), getattr(retry_state.
            next_action, 'sleep'), verb, value)
    return log_it