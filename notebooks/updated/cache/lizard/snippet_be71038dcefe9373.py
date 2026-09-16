def _should_retry(resp):
    return (resp.status_code == httplib.REQUEST_TIMEOUT or resp.status_code >=
        500 and resp.status_code < 600)