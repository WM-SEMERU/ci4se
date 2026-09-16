def close(self, session):
    try:
        del self.sessions[session]
        return constants.StatusCode.success
    except KeyError:
        return constants.StatusCode.error_invalid_object