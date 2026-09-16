def add_feature(feature, package=None, source=None, limit_access=False,
    enable_parent=False, image=None, restart=False):
    cmd = ['DISM', '/Quiet', '/Image:{0}'.format(image) if image else
        '/Online', '/Enable-Feature', '/FeatureName:{0}'.format(feature)]
    if package:
        cmd.append('/PackageName:{0}'.format(package))
    if source:
        cmd.append('/Source:{0}'.format(source))
    if limit_access:
        cmd.append('/LimitAccess')
    if enable_parent:
        cmd.append('/All')
    if not restart:
        cmd.append('/NoRestart')
    return __salt__['cmd.run_all'](cmd)