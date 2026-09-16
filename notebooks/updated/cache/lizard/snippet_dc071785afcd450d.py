def iiif_image_handler(prefix=None, identifier=None, path=None, config=None,
    klass=None, auth=None, **args):
    if not auth or degraded_request(identifier) or auth.image_authz():
        if auth:
            logging.debug('Authorized for image %s' % identifier)
        i = IIIFHandler(prefix, identifier, config, klass, auth)
        try:
            return i.image_request_response(path)
        except IIIFError as e:
            return i.error_response(e)
    else:
        degraded_uri = host_port_prefix(config.host, config.port, prefix
            ) + '/' + identifier + '-deg/' + path
        logging.info('Redirection to degraded: %s' % degraded_uri)
        response = redirect(degraded_uri)
        response.headers['Access-control-allow-origin'] = '*'
        return response