def __call_stream(self, uri, params=None, method='get'):
    try:
        resp = self.__get_response(uri, params, method, True)
        assert resp.ok
    except AssertionError:
        raise BadRequest(resp.status_code)
    except Exception as e:
        log.error('Bad response: {}'.format(e), exc_info=True)
    else:
        return resp