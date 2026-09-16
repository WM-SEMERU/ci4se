def confirm(self, msg, _timeout=-1):
    return self.msgBox('confirm', _timeout=_timeout, msg=msg)