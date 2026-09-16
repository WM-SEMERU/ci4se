def close(self):
    try:
        self.p.stdin.write(bytes('X\n', 'utf-8'))
        self.p.stdin.flush()
    except IOError:
        self.report('could not send exit command')
    self.p.wait()
    try:
        os.remove(self.tmpfile)
    except FileNotFoundError:
        pass