def close(self, session):
    try:
        sess = self.sessions[session]
        if sess is not self:
            sess.close()
    except KeyError:
        return StatusCode.error_invalid_object