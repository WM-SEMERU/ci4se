def read(self, session, count):
    try:
        ret = self.sessions[session].read(count)
    except KeyError:
        return 0, StatusCode.error_invalid_object
    if ret[1] < 0:
        raise errors.VisaIOError(ret[1])
    return ret