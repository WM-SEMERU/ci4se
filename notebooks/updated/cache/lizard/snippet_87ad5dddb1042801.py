def wrap(function, *args, **kwargs):
    try:
        req = function(*args, **kwargs)
        logger.debug('Got %s: %s', req.status_code, req.content)
        if req.status_code == 200:
            return req
        else:
            raise ClientException(req.reason, req.content)
    except ClientException:
        raise
    except Exception as exc:
        raise ClientException(exc)