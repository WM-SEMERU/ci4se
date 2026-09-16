def release_api_class(self):
    cls = current_app.config['GITHUB_RELEASE_CLASS']
    if isinstance(cls, string_types):
        cls = import_string(cls)
    assert issubclass(cls, GitHubRelease)
    return cls