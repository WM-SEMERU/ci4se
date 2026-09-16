def parseAndSave(option, urlOrPaths, outDir=None, serverEndpoint=
    ServerEndpoint, verbose=Verbose, tikaServerJar=TikaServerJar,
    responseMimeType='application/json', metaExtension='_meta.json',
    services={'meta': '/meta', 'text': '/tika', 'all': '/rmeta'}):
    metaPaths = []
    paths = getPaths(urlOrPaths)
    for path in paths:
        if outDir is None:
            metaPath = path + metaExtension
        else:
            metaPath = os.path.join(outDir, os.path.split(path)[1] +
                metaExtension)
            log.info('Writing %s' % metaPath)
            with open(metaPath, 'w', 'utf-8') as f:
                f.write(parse1(option, path, serverEndpoint, verbose,
                    tikaServerJar, responseMimeType, services)[1] + '\n')
        metaPaths.append(metaPath)
    return metaPaths