def http_log_resp(resp, body):
    if not pyrax.get_http_debug():
        return
    log = logging.getLogger('pyrax')
    log.debug('RESP: %s\n%s', resp, resp.headers)
    if body:
        log.debug('RESP BODY: %s', body)