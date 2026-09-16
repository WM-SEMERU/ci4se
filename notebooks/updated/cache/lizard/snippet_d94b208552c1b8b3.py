def get_num_names(include_expired=False, proxy=None, hostport=None):
    assert proxy or hostport, 'Need proxy or hostport'
    if proxy is None:
        proxy = connect_hostport(hostport)
    schema = {'type': 'object', 'properties': {'count': {'type': 'integer',
        'minimum': 0}}, 'required': ['count']}
    count_schema = json_response_schema(schema)
    resp = {}
    try:
        if include_expired:
            resp = proxy.get_num_names_cumulative()
        else:
            resp = proxy.get_num_names()
        resp = json_validate(count_schema, resp)
        if json_is_error(resp):
            return resp
    except ValidationError as e:
        if BLOCKSTACK_DEBUG:
            log.exception(e)
        resp = {'error':
            'Server response did not match expected schema.  You are likely communicating with an out-of-date Blockstack node.'
            , 'http_status': 502}
        return resp
    except socket.timeout:
        log.error('Connection timed out')
        resp = {'error': 'Connection to remote host timed out.',
            'http_status': 503}
        return resp
    except socket.error as se:
        log.error('Connection error {}'.format(se.errno))
        resp = {'error': 'Connection to remote host failed.', 'http_status':
            502}
        return resp
    except Exception as ee:
        if BLOCKSTACK_DEBUG:
            log.exception(ee)
        log.error('Caught exception while connecting to Blockstack node: {}'
            .format(ee))
        resp = {'error':
            'Failed to contact Blockstack node.  Try again with `--debug`.',
            'http_status': 500}
        return resp
    return resp['count']