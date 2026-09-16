def get_setup_version(reponame):
    from param.version import Version
    return Version.setup_version(os.path.dirname(__file__), reponame,
        archive_commit='$Format:%h$')