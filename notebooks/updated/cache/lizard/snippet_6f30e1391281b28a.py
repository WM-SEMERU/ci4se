def _write_value(value, path):
    base_command = "echo '{0}' > {1}"
    if platform == 'win32':
        command = '{0} > NUL'.format(base_command)
    else:
        command = 'exec 2> /dev/null; {0}'.format(base_command)
    os.system(command.format(value, path))