def detectType(option, urlOrPaths, serverEndpoint=ServerEndpoint, verbose=
    Verbose, tikaServerJar=TikaServerJar, responseMimeType='text/plain',
    services={'type': '/detect/stream'}):
    paths = getPaths(urlOrPaths)
    return [detectType1(option, path, serverEndpoint, verbose,
        tikaServerJar, responseMimeType, services) for path in paths]