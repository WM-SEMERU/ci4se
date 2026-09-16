def info(self):
    proc = Popen(['fish', '--version'], stdout=PIPE, stderr=DEVNULL)
    version = proc.stdout.read().decode('utf-8').split()[-1]
    return 'Fish Shell {}'.format(version)