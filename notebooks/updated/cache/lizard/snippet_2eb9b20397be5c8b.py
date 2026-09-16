def _call_rpc(self, address, rpc_id, payload):
    status, response = self.hw.stream.send_rpc(address, rpc_id, payload,
        timeout=1.1)
    return response