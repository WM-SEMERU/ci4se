def create_commit(self, message):
    cmd = self._command.commit(message)
    code, stdout, stderr = self._exec(cmd)
    if code:
        raise errors.VCSError(
            'Commit failed. Process exited with code %d and message: %s' %
            (code, stderr or stdout))