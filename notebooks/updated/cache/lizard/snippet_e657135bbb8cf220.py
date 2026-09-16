def shell(cmd, output=None, mode='w', cwd=None, shell=False):
    if not output:
        output = os.devnull
    else:
        folder = os.path.dirname(output)
        if folder and not os.path.isdir(folder):
            os.makedirs(folder)
    if not isinstance(cmd, (list, tuple)) and not shell:
        cmd = shlex.split(cmd)

    def run_shell():
        try:
            p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE, cwd=cwd,
                shell=shell)
        except OSError as e:
            logger.error(e)
            if e.errno == os.errno.ENOENT:
                logger.error("maybe you haven't installed %s", cmd[0])
            return e
        stdout, stderr = p.communicate()
        if stderr:
            logger.error(stderr)
            return stderr
        if PY3:
            stdout = stdout.decode()
        with open(output, mode) as f:
            f.write(stdout)
    return run_shell