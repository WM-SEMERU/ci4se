def find_resource_list_from_source_description(self, uri):
    self.logger.info('Reading source description %s' % uri)
    try:
        sd = SourceDescription()
        sd.read(uri=uri)
    except Exception as e:
        raise ClientError("Can't read source description from %s (%s)" % (
            uri, str(e)))
    if len(sd) == 0:
        raise ClientFatalError('Source description %s has no sources' % uri)
    elif len(sd) > 1:
        raise ClientFatalError(
            'Source description %s has multiple sources, specify one with --capabilitylist'
             % uri)
    self.logger.info('Finished reading source description')
    cluri = sd.resources.first().uri
    uri = urljoin(uri, cluri)
    return self.find_resource_list_from_capability_list(uri)