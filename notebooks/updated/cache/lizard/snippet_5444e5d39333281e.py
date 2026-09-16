def request_propagates(self, req_keys):
    i = 0
    for digest in req_keys:
        if digest not in self.requested_propagates_for:
            if digest not in self.requests:
                self.request_msg(PROPAGATE, {f.DIGEST.nm: digest})
            else:
                send_to = [conn for conn in self.nodestack.connecteds if 
                    conn not in self.requests[digest].propagates.keys()]
                self.request_msg(PROPAGATE, {f.DIGEST.nm: digest}, frm=send_to)
            self._add_to_recently_requested(digest)
            i += 1
        else:
            logger.debug('{} already requested PROPAGATE recently for {}'.
                format(self, digest))
    return i