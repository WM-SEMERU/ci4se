def get_resource(url, subdomain):
    headers = {'Accept': 'application/vnd.collection+json'}
    response = IASYSTEM_DAO().getURL(url, headers, subdomain)
    logger.info('%s ==status==> %s' % (url, response.status))
    if response.status != 200:
        logger.error('%s ==data==> %s' % (url, response.data))
        raise DataFailureException(url, response.status, response.data)
    return json.loads(response.data)