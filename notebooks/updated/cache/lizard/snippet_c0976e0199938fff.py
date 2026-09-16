def prepareSystem(cls):
    try:
        resourceRootDirPath = os.environ[cls.rootDirPathEnvName]
    except KeyError:
        resourceRootDirPath = mkdtemp()
        os.environ[cls.rootDirPathEnvName] = resourceRootDirPath
    assert os.path.isdir(resourceRootDirPath)