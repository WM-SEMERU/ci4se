def handle_ignored_resources(self):
    if self.method in ('GET', 'HEAD'
        ) and self.request.path_qs in self.IGNORED_PATHS:
        raise_404(self)