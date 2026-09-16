def put(self, path, args, wait=False):
    uri = self.make_uri(path)
    timeout = self.make_timeout(wait)
    try:
        logger.debug('put: %s, timeout: %s, params: %s', uri, timeout, args)
        rsp = self._requests_con.put(uri, args, timeout=timeout, verify=
            self.strong_ssl)
        logger.debug('got: %d - %s', rsp.status_code, rsp.text)
        if rsp.status_code != 200:
            raise HTTPClientDataException(rsp.status_code, rsp.text, uri)
        return rsp.content
    except (requests.Timeout, requests.ConnectTimeout):
        raise HTTPClientTimeoutException(timeout, uri)
    except requests.ConnectionError as exp:
        raise HTTPClientConnectionException(uri, exp.args[0])
    except Exception as exp:
        raise HTTPClientException('Request error to %s: %s' % (uri, exp))