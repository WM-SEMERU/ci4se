def get_setup_version(reponame):
    import json
    basepath = os.path.split(__file__)[0]
    version_file_path = os.path.join(basepath, reponame, '.version')
    try:
        from param import version
        assert hasattr(version, 'Version')
    except:
        version = embed_version(basepath)
    if version is not None:
        return version.Version.setup_version(basepath, reponame,
            archive_commit='$Format:%h$')
    else:
        print(
            'WARNING: param>=1.6.0 unavailable. If you are installing a package, this warning can safely be ignored. If you are creating a package or otherwise operating in a git repository, you should install param>=1.6.0.'
            )
        return json.load(open(version_file_path, 'r'))['version_string']