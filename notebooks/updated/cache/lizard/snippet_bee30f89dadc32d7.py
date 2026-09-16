def act(self):
    g = get_root(self).globals
    g.clog.info('\nSaving current application to disk')
    if not g.ipars.check():
        g.clog.warn('Invalid instrument parameters; save failed.')
        return False
    rok, msg = g.rpars.check()
    if not rok:
        g.clog.warn('Invalid run parameters; save failed.')
        g.clog.warn(msg)
        return False
    data = createJSON(g, full=False)
    if saveJSON(g, data):
        g.observe.load.enable()
        g.observe.unfreeze.disable()
        g.ipars.unfreeze()
        g.rpars.unfreeze()
        return True
    else:
        return False