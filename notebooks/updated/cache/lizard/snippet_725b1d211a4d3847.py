def current_id(self):
    cmd = ['hg', '-q', 'id', '-i']
    return self.sh(cmd, shell=False).rstrip().rstrip('+')