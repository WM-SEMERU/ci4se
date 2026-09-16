def check_python(cls):
    python_version = sys.version_info[:3]
    v_string = [str(i) for i in python_version]
    if python_version[0] == 2:
        python_version_s = '.'.join(v_string)
        if python_version[0] == 2 and python_version[1
            ] >= 7 and python_version[2] >= 9:
            print('You are running a supported version of python: {:}'.
                format(python_version_s))
        else:
            print(
                'WARNING: You are running an unsupported version of python: {:}'
                .format(python_version_s))
            print('         We recommend you update your python')
    elif python_version[0] == 3:
        python_version_s = '.'.join(v_string)
        if python_version[0] == 3 and python_version[1
            ] >= 7 and python_version[2] >= 0:
            print('You are running a supported version of python: {:}'.
                format(python_version_s))
        else:
            print(
                'WARNING: You are running an unsupported version of python: {:}'
                .format(python_version_s))
            print('         We recommend you update your python')
    python_version, pip_version = cls.get_python()
    if int(pip_version.split('.')[0]) >= 18:
        print('You are running a supported version of pip: ' + str(pip_version)
            )
    else:
        print('WARNING: You are running an old version of pip: ' + str(
            pip_version))
        print('         We recommend you update your pip  with \n')
        print('             pip install -U pip\n')