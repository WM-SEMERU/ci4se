def print_stack(pid, include_greenlet=False, debugger=None, verbose=False):
    sys_stdout = getattr(sys.stdout, 'buffer', sys.stdout)
    sys_stderr = getattr(sys.stderr, 'buffer', sys.stderr)
    make_args = make_gdb_args
    environ = dict(os.environ)
    if debugger == 'lldb' or debugger is None and platform.system().lower(
        ) == 'darwin':
        make_args = make_lldb_args
        environ['PATH'] = '/usr/bin:%s' % environ.get('PATH', '')
    tmp_fd, tmp_path = tempfile.mkstemp()
    os.chmod(tmp_path, 511)
    commands = []
    commands.append(FILE_OPEN_COMMAND)
    commands.extend(UTILITY_COMMANDS)
    commands.extend(THREAD_STACK_COMMANDS)
    if include_greenlet:
        commands.extend(GREENLET_STACK_COMMANDS)
    commands.append(FILE_CLOSE_COMMAND)
    command = ';'.join(commands)
    args = make_args(pid, command % tmp_path)
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=
        subprocess.PIPE)
    out, err = process.communicate()
    if verbose:
        sys_stderr.write(b'Standard Output:\n%s\n' % out)
        sys_stderr.write(b'Standard Error:\n%s\n' % err)
        sys_stderr.flush()
    for chunk in iter(functools.partial(os.read, tmp_fd, 1024), b''):
        sys_stdout.write(chunk)
    sys_stdout.write(b'\n')
    sys_stdout.flush()