def contents(self, path):
    try:
        out, code, err = self.command_exec(['cat-file', '-p', self.ref_head +
            ':' + path])
        if not code:
            return out.decode('utf-8')
    except Exception:
        pass
    return None