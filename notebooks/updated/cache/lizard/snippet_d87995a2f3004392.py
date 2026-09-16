def fetch_response(self, req_payload, **kwargs):
    if req_payload.uuid:
        uuids = set([req_payload.uuid, 'CONNECT'])

        def callback(res_payload):
            ret = res_payload.uuid in uuids
            if ret:
                logger.debug('{} received {} response for {}'.format(self.
                    client_id, res_payload.code, res_payload.uuid))
            return ret
        res_payload = self.recv_callback(callback, **kwargs)
    return res_payload