def load_ipython_extension(ip):
    if not getattr(ip, 'kernel'):
        warnings.warn(
            "wurlitzer extension doesn't do anything in terminal IPython")
        return
    ip.events.register('pre_execute', sys_pipes_forever)
    ip.events.register('post_execute', stop_sys_pipes)