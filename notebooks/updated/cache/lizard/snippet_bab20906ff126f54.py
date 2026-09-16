def _ignore_request(self, path):
    return any([re.match(pattern, path) for pattern in QC_SETTINGS[
        'IGNORE_REQUEST_PATTERNS']])