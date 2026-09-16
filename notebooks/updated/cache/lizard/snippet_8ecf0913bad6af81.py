def get_executable():
    pymap = {}
    with open(os.path.join(OPTIONS.saltdir, 'supported-versions')) as _fp:
        for line in _fp.readlines():
            ns, v_maj, v_min = line.strip().split(':')
            pymap[ns] = int(v_maj), int(v_min)
    pycmds = (sys.executable, 'python3', 'python27', 'python2.7',
        'python26', 'python2.6', 'python2', 'python')
    for py_cmd in pycmds:
        cmd = (py_cmd +
            ' -c  "import sys; sys.stdout.write(\'%s:%s\' % (sys.version_info[0], sys.version_info[1]))"'
            )
        stdout, _ = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=
            subprocess.PIPE, shell=True).communicate()
        if sys.version_info[0] == 2 and sys.version_info[1] < 7:
            stdout = stdout.decode(get_system_encoding(), 'replace').strip()
        else:
            stdout = stdout.decode(encoding=get_system_encoding(), errors=
                'replace').strip()
        if not stdout:
            continue
        c_vn = tuple([int(x) for x in stdout.split(':')])
        for ns in pymap:
            if c_vn[0] == pymap[ns][0] and c_vn >= pymap[ns
                ] and os.path.exists(os.path.join(OPTIONS.saltdir, ns)):
                return py_cmd
    sys.exit(EX_THIN_PYTHON_INVALID)