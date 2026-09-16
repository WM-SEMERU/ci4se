def sendall_stderr(self, s):
    while s:
        sent = self.send_stderr(s)
        s = s[sent:]
    return None