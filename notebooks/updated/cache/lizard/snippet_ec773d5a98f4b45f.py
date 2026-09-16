def open(self, user=None, repo=None):
    webbrowser.open(self.format_path(repo, namespace=user, rw=False))