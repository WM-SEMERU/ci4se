def shell_notify(msg, state=False, more=None, exitcode=None, verbose=True):
    if state is True:
        state = '[FATAL]'
        exitcode = 23
    elif state is None:
        state = '[WARNING]'
    elif state is False:
        state = '~'
    else:
        state = '[%s]' % str(state)
    m = ' %s %s' % (state, str(msg))
    if more:
        m += '\n\t' + _pformat(more).replace('\n', '\n\t')
    if verbose or isinstance(exitcode, int):
        print(m)
    if isinstance(exitcode, int):
        _exit(exitcode)
    return dict(message=msg, more=more, verbose=verbose)