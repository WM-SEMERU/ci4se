def run_cmd(call, cmd, *, echo=True, **kwargs):
    if echo:
        print('$> ' + ' '.join(map(pipes.quote, cmd)))
    return call(cmd, **kwargs)