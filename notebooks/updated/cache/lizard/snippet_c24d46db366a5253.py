def _escape_arg(self, arg):
    if self.winrm:
        return arg
    return ''.join([('\\' + char if re.match('\\W', char) else char) for
        char in arg])