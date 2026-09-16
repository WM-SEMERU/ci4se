def addPharLapPaths(env):
    ph_path = getPharLapPath()
    try:
        env_dict = env['ENV']
    except KeyError:
        env_dict = {}
        env['ENV'] = env_dict
    SCons.Util.AddPathIfNotExists(env_dict, 'PATH', os.path.join(ph_path,
        'bin'))
    SCons.Util.AddPathIfNotExists(env_dict, 'INCLUDE', os.path.join(ph_path,
        'include'))
    SCons.Util.AddPathIfNotExists(env_dict, 'LIB', os.path.join(ph_path, 'lib')
        )
    SCons.Util.AddPathIfNotExists(env_dict, 'LIB', os.path.join(ph_path, os
        .path.normpath('lib/vclib')))
    env['PHARLAP_PATH'] = getPharLapPath()
    env['PHARLAP_VERSION'] = str(getPharLapVersion())