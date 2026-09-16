def log(verbose=False):
    terminal.log.config(verbose=verbose)
    terminal.log.info('this is a info message')
    terminal.log.verbose.info('this is a verbose message')