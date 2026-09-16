def restart(self, reset=False):
    spyder_start_directory = get_module_path('spyder')
    restart_script = osp.join(spyder_start_directory, 'app', 'restart.py')
    env = os.environ.copy()
    bootstrap_args = env.pop('SPYDER_BOOTSTRAP_ARGS', None)
    spyder_args = env.pop('SPYDER_ARGS')
    pid = os.getpid()
    python = sys.executable
    if bootstrap_args is not None:
        spyder_args = bootstrap_args
        is_bootstrap = True
    else:
        is_bootstrap = False
    env['SPYDER_ARGS'] = spyder_args
    env['SPYDER_PID'] = str(pid)
    env['SPYDER_IS_BOOTSTRAP'] = str(is_bootstrap)
    env['SPYDER_RESET'] = str(reset)
    if DEV:
        if os.name == 'nt':
            env['PYTHONPATH'] = ';'.join(sys.path)
        else:
            env['PYTHONPATH'] = ':'.join(sys.path)
    if os.name == 'nt':
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        shell = False
    else:
        startupinfo = None
        shell = True
    command = '"{0}" "{1}"'
    command = command.format(python, restart_script)
    try:
        if self.closing(True):
            subprocess.Popen(command, shell=shell, env=env, startupinfo=
                startupinfo)
            self.console.quit()
    except Exception as error:
        print(error)
        print(command)