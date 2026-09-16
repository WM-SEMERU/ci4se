def __monkey_patch_juman_lines(self, input_str):
    assert isinstance(self.juman, pyknp.Juman)
    if not self.juman.socket and not self.juman.subprocess:
        if self.juman.server is not None:
            self.juman.socket = MonkeyPatchSocket(self.juman.server, self.
                juman.port, b'RUN -e2\n')
        else:
            command = '%s %s' % (self.juman.command, self.juman.option)
            if self.juman.rcfile:
                command += ' -r %s' % self.juman.rcfile
            self.juman.subprocess = pyknp.Subprocess(command)
    if self.juman.socket:
        return self.juman.socket.query(input_str, pattern=self.juman.pattern)
    return self.juman.subprocess.query(input_str, pattern=self.juman.pattern)