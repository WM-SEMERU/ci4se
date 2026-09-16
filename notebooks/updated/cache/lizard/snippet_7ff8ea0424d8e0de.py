def remove_capability(capability, image=None, restart=False):
    if salt.utils.versions.version_cmp(__grains__['osversion'], '10') == -1:
        raise NotImplementedError(
            '`uninstall_capability` is not available on this version of Windows: {0}'
            .format(__grains__['osversion']))
    cmd = ['DISM', '/Quiet', '/Image:{0}'.format(image) if image else
        '/Online', '/Remove-Capability', '/CapabilityName:{0}'.format(
        capability)]
    if not restart:
        cmd.append('/NoRestart')
    return __salt__['cmd.run_all'](cmd)