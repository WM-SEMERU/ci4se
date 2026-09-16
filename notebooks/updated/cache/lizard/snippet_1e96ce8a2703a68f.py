def process_response(self, req, resp, resource):
    if 'result' not in req.context:
        return
    req.context['result']['is_login'] = 'user_id' in req.env['session']
    if settings.DEBUG:
        req.context['result']['_debug_queries'] = sys._debug_db_queries
        sys._debug_db_queries = []
    if resp.body is None and req.context['result']:
        resp.body = json.dumps(req.context['result'])
    try:
        log.debug('RESPONSE: %s' % resp.body)
    except:
        log.exception('ERR: RESPONSE CANT BE LOGGED ')