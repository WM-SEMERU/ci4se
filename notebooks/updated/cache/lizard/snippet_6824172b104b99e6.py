def get_complex_output(self, stderr=STDOUT):
    proc = Popen(self.cmd, shell=True, stdout=PIPE, stderr=stderr)
    return proc.stdout.readlines()