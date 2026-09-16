def createFromURL(urlOfXMLDefinition):
    url = urlparse(urlOfXMLDefinition)
    if not url.port:
        if url.scheme.lower() == 'https':
            port = 443
        else:
            port = 80
    else:
        port = url.port
    return Wifi(url.hostname, port, url.scheme)