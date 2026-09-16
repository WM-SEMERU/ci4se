def log_param(name, value):
    log('setting {} = {}', click.style(str(name)), click.style(str(value),
        fg='yellow'))