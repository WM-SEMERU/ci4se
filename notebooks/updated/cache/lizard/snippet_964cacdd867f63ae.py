def invoke_shell(self, locs, banner):
    shell = self.SHELLS[self.args.shell]
    try:
        shell().invoke(locs, banner)
    except ImportError as e:
        warn('%s is not installed, `%s`, falling back to native shell' % (
            self.args.shell, e), RuntimeWarning)
        if shell == NativePythonShell:
            raise
        NativePythonShell().invoke(locs, banner)