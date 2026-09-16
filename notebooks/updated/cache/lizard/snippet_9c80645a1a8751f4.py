def UpdateManifestResourcesFromXMLFile(dstpath, srcpath, names=None,
    languages=None):
    logger.info('Updating manifest from %s in %s', srcpath, dstpath)
    if dstpath.lower().endswith('.exe'):
        name = 1
    else:
        name = 2
    winresource.UpdateResourcesFromDataFile(dstpath, srcpath, RT_MANIFEST, 
        names or [name], languages or [0, '*'])