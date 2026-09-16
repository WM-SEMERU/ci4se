def find_eigen(hint=None):
    r
    try:
        import pkgconfig
        if pkgconfig.installed('eigen3', '>3.0.0'):
            return pkgconfig.parse('eigen3')['include_dirs'][0]
    except:
        pass
    search_dirs = [] if hint is None else hint
    search_dirs += ['/usr/local/include/eigen3',
        '/usr/local/homebrew/include/eigen3',
        '/opt/local/var/macports/software/eigen3',
        '/opt/local/include/eigen3', '/usr/include/eigen3',
        '/usr/include/local', '/usr/include']
    for d in search_dirs:
        path = os.path.join(d, 'Eigen', 'Dense')
        if os.path.exists(path):
            vf = os.path.join(d, 'Eigen', 'src', 'Core', 'util', 'Macros.h')
            if not os.path.exists(vf):
                continue
            src = open(vf, 'r').read()
            v1 = re.findall('#define EIGEN_WORLD_VERSION (.+)', src)
            v2 = re.findall('#define EIGEN_MAJOR_VERSION (.+)', src)
            v3 = re.findall('#define EIGEN_MINOR_VERSION (.+)', src)
            if not len(v1) or not len(v2) or not len(v3):
                continue
            v = '{0}.{1}.{2}'.format(v1[0], v2[0], v3[0])
            print('Found Eigen version {0} in: {1}'.format(v, d))
            return d
    return None