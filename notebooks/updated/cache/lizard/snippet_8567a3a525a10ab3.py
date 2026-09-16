def _get_path_pattern_tornado4(self):
    for host, handlers in self.application.handlers:
        if host.match(self.request.host):
            for handler in handlers:
                if handler.regex.match(self.request.path):
                    return handler.regex.pattern