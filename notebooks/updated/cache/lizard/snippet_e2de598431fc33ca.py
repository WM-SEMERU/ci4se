def redirect_stds(self):
    if not self.debug:
        sys.stdout = self.stdout_write
        sys.stderr = self.stderr_write
        sys.stdin = self.stdin_read