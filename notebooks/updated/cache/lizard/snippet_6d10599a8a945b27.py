def _get_url(self, path, base=JIRA_BASE_URL):
    options = self._options.copy()
    options.update({'path': path})
    return base.format(**options)