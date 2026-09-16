def start(name):
    ret = {}
    cmd = '{0} startvm {1}'.format(vboxcmd(), name)
    ret = salt.modules.cmdmod.run(cmd).splitlines()
    return ret