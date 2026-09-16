def _handle_exception(ignore_callback_errors, print_callback_errors, obj,
    cb_event=None, node=None):
    if not hasattr(obj, '_vispy_err_registry'):
        obj._vispy_err_registry = {}
    registry = obj._vispy_err_registry
    if cb_event is not None:
        cb, event = cb_event
        exp_type = 'callback'
    else:
        exp_type = 'node'
    type_, value, tb = sys.exc_info()
    tb = tb.tb_next
    sys.last_type = type_
    sys.last_value = value
    sys.last_traceback = tb
    del tb
    if not ignore_callback_errors:
        raise
    if print_callback_errors != 'never':
        this_print = 'full'
        if print_callback_errors in ('first', 'reminders'):
            if exp_type == 'callback':
                key = repr(cb) + repr(event)
            else:
                key = repr(node)
            if key in registry:
                registry[key] += 1
                if print_callback_errors == 'first':
                    this_print = None
                else:
                    ii = registry[key]
                    if ii == 2 ** int(np.log2(ii)):
                        this_print = ii
                    else:
                        this_print = None
            else:
                registry[key] = 1
        if this_print == 'full':
            logger.log_exception()
            if exp_type == 'callback':
                logger.error('Invoking %s for %s' % (cb, event))
            else:
                logger.error('Drawing node %s' % node)
        elif this_print is not None:
            if exp_type == 'callback':
                logger.error('Invoking %s repeat %s' % (cb, this_print))
            else:
                logger.error('Drawing node %s repeat %s' % (node, this_print))