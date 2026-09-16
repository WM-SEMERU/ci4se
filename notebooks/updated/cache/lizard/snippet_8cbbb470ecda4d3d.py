def get_account_tokens(address, hostport=None, proxy=None):
    assert proxy or hostport, 'Need proxy or hostport'
    if proxy is None:
        proxy = connect_hostport(hostport)
    tokens_schema = {'type': 'object', 'properties': {'token_types': {
        'type': 'array', 'pattern': '^(.+){1,19}'}}, 'required': [
        'token_types']}
    schema = json_response_schema(tokens_schema)
    try:
        resp = proxy.get_account_tokens(address)
        resp = json_validate(schema, resp)
        if json_is_error(resp):
            return resp
    except ValidationError as ve:
        if BLOCKSTACK_DEBUG:
            log.exception(ve)
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
    except AssertionError as ae:
        if BLOCKSTACK_DEBUG:
            log.exception(ae)
        resp = json_traceback(resp.get('error'))
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
    resp['token_types'].sort()
    return resp['token_types']