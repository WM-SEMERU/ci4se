def _process_exlist(self, exc, raised):
    if not raised or raised and exc.endswith('*'):
        return exc[:-1] if exc.endswith('*') else exc
    return None