def garbage_collection(time_limit=YEAR / 12.0):
    expired_request_infos = (ri for ri in DATABASE.values() if ri.
        creation_ts + time_limit <= time.time())
    for ri in expired_request_infos:
        del DATABASE[ri.url]