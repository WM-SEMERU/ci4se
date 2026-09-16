def run(self):
    command = ['npm', 'install']
    self.announce('Running command: %s' % str(command), level=INFO)
    subprocess.check_call(command)