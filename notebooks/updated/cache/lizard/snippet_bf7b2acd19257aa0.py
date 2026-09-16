def send_rpc_sync(self, conn_id, address, rpc_id, payload, timeout):
    done = threading.Event()
    result = {}

    def send_rpc_done(conn_id, adapter_id, status, reason, rpc_status,
        resp_payload):
        result['success'] = status
        result['failure_reason'] = reason
        result['status'] = rpc_status
        result['payload'] = resp_payload
        done.set()
    self.send_rpc_async(conn_id, address, rpc_id, payload, timeout,
        send_rpc_done)
    done.wait()
    return result