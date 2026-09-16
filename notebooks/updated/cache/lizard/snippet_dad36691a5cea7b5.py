def detectType1(option, urlOrPath, serverEndpoint=ServerEndpoint, verbose=
    Verbose, tikaServerJar=TikaServerJar, responseMimeType='text/plain',
    services={'type': '/detect/stream'}, config_path=None):
    path, mode = getRemoteFile(urlOrPath, TikaFilesPath)
    if option not in services:
        log.exception('Detect option must be one of %s' % binary_string(
            services.keys()))
        raise TikaException('Detect option must be one of %s' %
            binary_string(services.keys()))
    service = services[option]
    status, response = callServer('put', serverEndpoint, service, open(path,
        'rb'), {'Accept': responseMimeType, 'Content-Disposition':
        make_content_disposition_header(path)}, verbose, tikaServerJar,
        config_path=config_path)
    if csvOutput == 1:
        return status, urlOrPath.decode('UTF-8') + ',' + response
    else:
        return status, response