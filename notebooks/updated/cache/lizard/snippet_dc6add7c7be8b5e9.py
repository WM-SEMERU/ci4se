def get(cls, session, record_id, endpoint_override=None):
    cls._check_implements('get')
    try:
        return cls(endpoint_override or '/%s/%d.json' % (cls.__endpoint__,
            record_id), singleton=True, session=session)
    except HelpScoutRemoteException as e:
        if e.status_code == 404:
            return None
        else:
            raise