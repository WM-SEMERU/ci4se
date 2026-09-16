def write_pid(pidfile):
    pid = str(os.getpid())
    try:
        with open(pidfile, mode='w') as _file:
            print('writing processID {p} to pidfile'.format(p=pid))
            _file.write(pid)
    except OSError as exc:
        sys.exit('failed to write pidfile:{e}'.format(e=exc))