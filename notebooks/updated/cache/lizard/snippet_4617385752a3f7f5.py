def safeprint(message, write_to_stderr=False, newline=True):
    try:
        click.echo(message, nl=newline, err=write_to_stderr)
    except IOError as err:
        if err.errno is errno.EPIPE:
            pass
        else:
            raise