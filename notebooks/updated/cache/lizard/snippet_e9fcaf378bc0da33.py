def parse_resource_type(self, response):
    links = [link.split(';')[0].lstrip('<').rstrip('>') for link in
        response.headers['Link'].split(', ') if link.startswith(
        '<http://www.w3.org/ns/ldp#')]
    ldp_resource_types = [self.repo.namespace_manager.compute_qname(
        resource_type)[2] for resource_type in links]
    logger.debug('Parsed LDP resource types from LINK header: %s' %
        ldp_resource_types)
    if 'NonRDFSource' in ldp_resource_types:
        return NonRDFSource
    elif 'BasicContainer' in ldp_resource_types:
        return BasicContainer
    elif 'DirectContainer' in ldp_resource_types:
        return DirectContainer
    elif 'IndirectContainer' in ldp_resource_types:
        return IndirectContainer
    else:
        logger.debug(
            'could not determine resource type from Link header, returning False'
            )
        return False