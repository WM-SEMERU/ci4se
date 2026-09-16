def getCollectionClass(cls, name):
    try:
        return cls.collectionClasses[name]
    except KeyError:
        raise KeyError(
            "There is no Collection Class of type: '%s'; currently supported values: [%s]"
             % (name, ', '.join(getCollectionClasses().keys())))